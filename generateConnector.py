#!/usr/bin/env python3
import json
import re
from pathlib import Path

# ---------- Helpers to detect SQL types ----------
def is_string_type(t: str) -> bool:
    if not t: return False
    t = t.upper()
    return any(x in t for x in ("CHAR", "TEXT", "VARCHAR"))

def is_date_type(t: str) -> bool:
    if not t: return False
    t = t.upper()
    return "DATE" in t or "DATETIME" in t or "TIMESTAMP" in t

def is_bool_type(t: str) -> bool:
    if not t: return False
    t = t.upper()
    return "BOOLEAN" in t or re.search(r"TINYINT\s*\(\s*1\s*\)", t) is not None or "BOOL" in t

def is_int_type(t: str) -> bool:
    if not t: return False
    t = t.upper()
    # exclude tinyint(1) handled as bool
    return "INT" in t and not is_bool_type(t)

def is_json_type(t: str) -> bool:
    if not t: return False
    return "JSON" in t.upper()

# ---------- Read schema ----------
schema_path = Path("Tables.json")
if not schema_path.exists():
    raise FileNotFoundError("Tables.json not found in current directory.")

with open(schema_path, "r", encoding="utf-8") as f:
    schema = json.load(f)

# ---------- Header (imports + string_to_date) ----------
header = '''import mysql.connector
import json
from mysql.connector import Error
from datetime import date
from datetime import datetime

def string_to_date(date_string: str) -> datetime.date:
    if date_string:
        try:
            return datetime.strptime(date_string, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format. Expected 'yyyy-mm-dd', got {date_string}")
    else: 
        return None
'''

# ---------- Build get_functions ----------
get_class_lines = []
get_class_lines.append("\nclass get_functions():")
for table_name, cols in schema.items():
    # Keep column order
    columns = list(cols.keys())
    # skip if no columns
    if not columns:
        continue
    id_field = "id"
    non_id_cols = [c for c in columns if c != id_field]

    # determine parameter defaults based on types
    params = []
    for c in non_id_cols:
        t = cols[c] if isinstance(cols[c], str) else str(cols[c])
        if is_string_type(t):
            params.append(f"{c}=''")
        else:
            params.append(f"{c}=None")
    # id param first
    signature_params = ["id=None"] + params

    func_name = f"get_{table_name.lower()}"
    get_class_lines.append(f"\n    @staticmethod")
    get_class_lines.append(f"    def {func_name}(connection, {', '.join(signature_params)}):")
    get_class_lines.append(f"        cursor = connection.cursor()")

    # convert date-like params using string_to_date (any param whose name contains 'date', 'onset', 'dob', 'birthday')
    for c in non_id_cols:
        t = cols[c] if isinstance(cols[c], str) else str(cols[c])
        lower = c.lower()
        if is_date_type(t) or any(k in lower for k in ("date", "onset", "dob", "birthday")):
            get_class_lines.append(f"        {c} = string_to_date({c})")

    get_class_lines.append(f"        # Start building the base query")
    # Use lowercased table name in SQL to match original style in many places; but if schema table contains underscores & capitals keep it as-is:
    sql_table = table_name if "_" in table_name else table_name.lower()
    get_class_lines.append(f"        query = \"SELECT * FROM {sql_table} WHERE 1=1\"")
    get_class_lines.append(f"        filters = []")
    get_class_lines.append("")

    # id handling
    get_class_lines.append(f"        if id is not None:")
    get_class_lines.append(f"            query += \" AND id = %s\"")
    get_class_lines.append(f"            filters.append(id)")
    get_class_lines.append("")

    # other columns: strings -> LIKE (if truthy), others -> equality when not None
    for c in non_id_cols:
        t = cols[c] if isinstance(cols[c], str) else str(cols[c])
        if is_string_type(t):
            # truthy check matches original (if staff_name:)
            get_class_lines.append(f"        if {c}:")
            get_class_lines.append(f"            query += \" AND {c} LIKE %s\"")
            get_class_lines.append(f"            filters.append(f'%{{{c}}}%')")
            get_class_lines.append("")
        else:
            # date, bool, int, json -> equality if not None
            get_class_lines.append(f"        if {c} is not None:")
            get_class_lines.append(f"            query += \" AND {c} = %s\"")
            get_class_lines.append(f"            filters.append({c})")
            get_class_lines.append("")

    # execute
    get_class_lines.append(f"        # Execute the query with filters")
    get_class_lines.append(f"        cursor.execute(query, tuple(filters))")
    get_class_lines.append(f"        # Fetch all results")
    get_class_lines.append(f"        results = cursor.fetchall()")
    get_class_lines.append("")

    # build dict_results: decode JSON columns specially
    get_class_lines.append(f"        dict_results = {{}}")
    # columns list for output: use same order as schema
    col_list_repr = "[" + ", ".join([f'\"{c}\"' for c in columns]) + "]"
    get_class_lines.append(f"        columns = {col_list_repr}")
    get_class_lines.append(f"        for i in range(len(columns)):")
    # inside loop: check if column is JSON type using schema info
    # We'll produce code that checks column name against a set of JSON columns for this table.
    json_cols = [c for c, t in cols.items() if is_json_type(t if isinstance(t, str) else str(t))]
    if json_cols:
        json_cols_repr = "[" + ", ".join([f"\"{c}\"" for c in json_cols]) + "]"
        get_class_lines.append(f"            if columns[i] in {json_cols_repr}:")
        get_class_lines.append("                dict_results[columns[i]] = [")
        get_class_lines.append("                    json.loads(results[j][i]) if results[j][i] and results[j][i] != \"None\" else None")
        get_class_lines.append("                    for j in range(len(results))")
        get_class_lines.append("                ]")
        get_class_lines.append("            else:")
        get_class_lines.append("                dict_results[columns[i]] = [str(results[j][i]) for j in range(len(results))]")
    else:
        get_class_lines.append("            dict_results[columns[i]] = [str(results[j][i]) for j in range(len(results))]")

    get_class_lines.append("        if connection:")
    get_class_lines.append("            connection.close()")
    get_class_lines.append("        return dict_results")

# ---------- Build update_functions ----------
update_class_lines = []
update_class_lines.append("\nclass update_functions():")
for table_name, cols in schema.items():
    columns = list(cols.keys())
    if not columns:
        continue
    id_field = "id"
    non_id_cols = [c for c in columns if c != id_field]

    # signature: connection, id, then params with same defaults used in get
    params = []
    for c in non_id_cols:
        t = cols[c] if isinstance(cols[c], str) else str(cols[c])
        if is_string_type(t):
            params.append(f"{c}=None")  # use None in update signature so caller can pass empty string intentionally if needed
        else:
            params.append(f"{c}=None")
    signature = ", ".join(["connection", "id"] + params)

    func_name = f"update_{table_name.lower()}"
    update_class_lines.append(f"\n    @staticmethod")
    update_class_lines.append(f"    def {func_name}({signature}):")
    update_class_lines.append("        cursor = connection.cursor()")
    update_class_lines.append(f"        update_query = \"UPDATE {table_name} SET \"")
    update_class_lines.append("        update_values = []")
    update_class_lines.append("")

    # For update logic: strings -> if param: (truthy), booleans/dates/ints -> if param is not None
    for c in non_id_cols:
        t = cols[c] if isinstance(cols[c], str) else str(cols[c])
        if is_string_type(t):
            update_class_lines.append(f"        if {c}:")
            update_class_lines.append(f"            update_query += \"{c} = %s, \"")
            update_class_lines.append(f"            update_values.append({c})")
        else:
            # include boolean/date/int/json with is not None (so False allowed)
            update_class_lines.append(f"        if {c} is not None:")
            # original file sometimes casts booleans to str for tour.strategies_used; not necessary
            update_class_lines.append(f"            update_query += \"{c} = %s, \"")
            update_class_lines.append(f"            update_values.append({c})")
        update_class_lines.append("")

    update_class_lines.append("        # Remove trailing comma and add WHERE clause")
    update_class_lines.append("        update_query = update_query.rstrip(\", \")")
    update_class_lines.append("        update_query += \" WHERE id = %s\"")
    update_class_lines.append("        update_values.append(id)")
    update_class_lines.append("")
    update_class_lines.append("        cursor.execute(update_query, tuple(update_values))")
    update_class_lines.append("        connection.commit()")
    update_class_lines.append("        if connection:")
    update_class_lines.append("            connection.close()")
    update_class_lines.append("        return id")

# ---------- Build insert_functions ----------
insert_class_lines = []
insert_class_lines.append("\nclass insert_functions():")
for table_name, cols in schema.items():
    columns = list(cols.keys())
    if not columns:
        continue
    id_field = "id"
    non_id_cols = [c for c in columns if c != id_field]

    # signature: connection, then parameters for all non-id columns (no defaults)
    params = ", ".join(["connection"] + non_id_cols)
    func_name = f"insert_{table_name.lower()}"
    insert_class_lines.append(f"\n    @staticmethod")
    insert_class_lines.append(f"    def {func_name}({params}):")
    insert_class_lines.append("        cursor = connection.cursor()")

    cols_sql = ", ".join(non_id_cols)
    placeholders = ", ".join(["%s"] * len(non_id_cols))
    insert_class_lines.append("        insert_query = \"\"\"")
    insert_class_lines.append(f"        INSERT INTO {table_name} (")
    # break columns across lines for readability
    # break into lines of up to ~6 columns per line
    if non_id_cols:
        chunk_size = 6
        for i in range(0, len(non_id_cols), chunk_size):
            chunk = non_id_cols[i:i+chunk_size]
            insert_class_lines.append("            " + ", ".join(chunk) + ("," if i + chunk_size < len(non_id_cols) else ""))
    insert_class_lines.append("        ) ")
    insert_class_lines.append("        VALUES (" + placeholders + ")")
    insert_class_lines.append("        \"\"\"")
    # Data tuple in same order
    data_tuple = ", ".join(non_id_cols)
    insert_class_lines.append("")
    insert_class_lines.append("        data = (")
    # break tuple lines similar to insert columns
    if non_id_cols:
        chunk_size = 6
        for i in range(0, len(non_id_cols), chunk_size):
            chunk = non_id_cols[i:i+chunk_size]
            insert_class_lines.append("            " + ", ".join(chunk) + ("," if i + chunk_size < len(non_id_cols) else ""))
    insert_class_lines.append("        )")
    insert_class_lines.append("")
    insert_class_lines.append("        cursor.execute(insert_query, data)")
    insert_class_lines.append("        connection.commit()")
    insert_class_lines.append("        if connection:")
    insert_class_lines.append("            connection.close()")
    insert_class_lines.append("        return cursor.lastrowid")

# ---------- Combine and write file ----------
out_path = Path("SQL_connector.py")
with open(out_path, "w", encoding="utf-8") as out_f:
    out_f.write(header)
    out_f.write("\n")
    out_f.write("\n".join(get_class_lines))
    out_f.write("\n")
    out_f.write("\n".join(update_class_lines))
    out_f.write("\n")
    out_f.write("\n".join(insert_class_lines))
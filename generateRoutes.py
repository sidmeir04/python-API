import json

# Load JSON schema
with open("Tables.json", "r") as f:
    schema = json.load(f)

# Boilerplate header
header = """from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import pooling
from mysql.connector import Error
from SQL_connector import *
import json

app = Flask(__name__)

db_config = {
    "host": "localhost",
    "user": "connector",
    "password": "password",
    "database": "adler_aphasia_center",
    "auth_plugin": "mysql_native_password"
}

# Create a connection pool
try:
    pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=32, **db_config)
    print("Database connection pool created successfully.")
except mysql.connector.Error as e:
    print(f"Error creating MySQL connection pool: {e}")
    pool = None

# Function to get a connection from the pool
def get_connection():
    if pool:
        return pool.get_connection()
    else:
        raise ConnectionError("No database connection pool available.")

"""

routes_code = header

# Loop through tables and generate Flask routes
for table_name, columns in schema.items():
    lower_name = table_name.lower()
    id_field = "id"
    fields = [col for col in columns.keys() if col != "id"]

    # GET
    routes_code += f"""
@app.route('/get_{lower_name}', methods=['POST'])
def get_{lower_name}():
    data = request.get_json()
    result = get_functions.get_{lower_name}(
        connection=get_connection(),
        {id_field}=data.get('{id_field}', None),
"""
    for col in fields:
        routes_code += f"        {col}=data.get('{col}', None),\n"
    routes_code += "    )\n"
    routes_code += f"    return jsonify(result), 200\n"

    # UPDATE
    routes_code += f"""
@app.route('/update_{lower_name}', methods=['POST'])
def update_{lower_name}():
    data = json.loads(request.get_json()[0])
    update_functions.update_{lower_name}(
        connection=get_connection(),
        {id_field}=data.get('{id_field}'),
"""
    for col in fields:
        routes_code += f"        {col}=data.get('{col}', None),\n"
    routes_code += "    )\n"
    routes_code += "    return '', 200\n"

    # INSERT
    routes_code += f"""
@app.route('/insert_{lower_name}', methods=['POST'])
def insert_{lower_name}():
    data = json.loads(request.get_json()[0])
    id = insert_functions.insert_{lower_name}(
        connection=get_connection(),
"""
    for col in fields:
        routes_code += f"        {col}=data.get('{col}', None),\n"
    routes_code += "    )\n"
    routes_code += "    return str(id), 200\n"

    # Running the file
routes_code += "if __name__ == \'__main__\':\n    app.run(debug=True)"

# Save everything into one file
with open("MYSQL_api.py", "w") as f:
    f.write(routes_code)
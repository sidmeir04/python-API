from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error
from SQL_connecter import get_functions

app = Flask(__name__)

# Sample data
data = [
    {"id": 1, "name": "Item 1", "description": "Description for Item 1"},
    {"id": 2, "name": "Item 2", "description": "Description for Item 2"},
    {"id": 3, "name": "Item 3", "description": "Description for Item 3"}
]

host = "localhost"
user = "connector"
password = "password"
database = "adler_aphasia_center"
connection = None
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        auth_plugin="mysql_native_password"
    )
except Error as e:
    print(f"The error '{e}' occurred")

# Home route
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# def get_caller(connection, staff_name='', caller_name='', caller_email = '', call_date=None, phone='', referral_type='', tour_scheduled=None, follow_up_date=None):
@app.route('/get_caller', methods=['GET'])
def get_caller():
    caller_data = request.get_json()
    caller = get_functions.get_caller(
        connection=connection,
        staff_name=caller_data.get('staff_name', ''),
        caller_name=caller_data.get('caller_name', ''),
        caller_email=caller_data.get('caller_email', ''),
        call_date=caller_data.get('call_date', None),
        phone=caller_data.get('phone', ''),
        referral_type=caller_data.get('referral_type', ''),
        tour_scheduled=caller_data.get('tour_scheduled', None),
        follow_up_date=caller_data.get('follow_up_date', None)
    )
    return jsonify(caller), 200

# def get_tour(connection,tour_date=None, attended=None, clinicians='', 
#                 strategies_used=None, aep_deadline=None, 
#                 joined_after=None, likely_to_join=None, 
#                 canceled=None):@app.route('/get_tour', methods=['GET'])
@app.route('/get_tour', methods=['GET'])
def get_tour():
    tour_data = request.get_json()
    tour = get_functions.get_tour(
        connection=connection,
        tour_date=tour_data.get('tour_date', None),
        attended=tour_data.get('attended', None),
        clinicians=tour_data.get('clinicians', ''),
        strategies_used=tour_data.get('strategies_used', None),
        aep_deadline=tour_data.get('aep_deadline', None),
        joined_after=tour_data.get('joined_after', None),
        likely_to_join=tour_data.get('likely_to_join', None),
        canceled=tour_data.get('canceled', None),
    )
    return jsonify(tour), 200

# def get_member(connection, name='', age=None, dob=None, email='', 
#                 aep_completion_date=None, join_date=None, 
#                 schedule=None, phone='', address='', 
#                 county='', gender='', veteran=None, 
#                 joined=None, caregiver_needed=None, alder_program=''):
@app.route('/get_member', methods=['GET'])
def get_member():
    member_data = request.get_json()
    member = get_functions.get_member(
        connection=connection,
        name=member_data.get('name', ''),
        age=member_data.get('age', None),
        dob=member_data.get('dob', None),
        email=member_data.get('email', ''),
        schedule=member_data.get('schedule', None),
        phone=member_data.get('phone', ''),
        address=member_data.get('address', ''),
        county=member_data.get('county', ''),
        gender=member_data.get('gender', ''),
        veteran=member_data.get('veteran', None),
        joined=member_data.get('joined', None),
        caregiver_needed=member_data.get('caregiver_needed', ''),
        alder_program=member_data.get('alder_program', ''),
    )
    return jsonify(member), 200


# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# Get a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

# Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item['id'] = max(item['id'] for item in data) + 1 if data else 1
    data.append(new_item)
    return jsonify(new_item), 201

# Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    updates = request.get_json()
    item.update(updates)
    return jsonify(item)

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [item for item in data if item['id'] != item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)

# Python API (Flask Backend for Adler Database)

This folder contains the **Python Flask API** that handles communication between the C++ frontend and the MySQL database. It provides endpoints for retrieving, updating, and inserting records for various components of the Adler Aphasia Center system.

## Overview

- Built using **Flask** and **MySQL Connector**
- Uses a **MySQL connection pool** for query handling
- Divided into classes for `get`, `update`, and `insert` operations
- Connects directly to a structured MySQL schema for member, caregiver, tour, and outreach data

## Files

- **`MYSQL_api.py`** – The main Flask app. Defines all API routes.
- **`SQL_connecter.py`** – Contains the SQL logic for fetching and manipulating data from MySQL using safe, dynamic queries.

## Key Features

- **Connection Pooling**: Uses `mysql.connector.pooling.MySQLConnectionPool` to handle several rapid requests.
- **Modular Query Logic**: Organized under `get_functions`, `update_functions`, and `insert_functions` classes.
- **Dynamic Filters**: GET endpoints build SQL `WHERE` clauses based on request body fields.
- **Flexible Integration**: Communicates with the C++ frontend via HTTP POST requests using JSON payloads.

## Running the API

1. Ensure MySQL is running and the Adler database has been created (see root README).
2. Set your database credentials inside `MYSQL_api.py`:

```python
db_config = {
    "host": "localhost",
    "user": "your_user",
    "password": "your_password",
    "database": "adler_aphasia_center",
    "auth_plugin": "mysql_native_password"
}
```
3. Currently the database in set to run on all avialable ports, so do not run on public wifi networks and if you are change it to only run on localhost. You can check where it is running based on the printout on startup
4. Run the API using VS Code or from terminal, either works fine

## Endpoints

For all the endpoints they expect a json file in order to get the parameters to search the database, if an empty one if provided it will cause an error

## Notes
- Date fields must be in "YYYY-MM-DD" format.
- Some endpoints expect special fields like JSON strings (e.g. member_info).
- When deploying the API make sure to remove debug=True
- Right now the feilds are manually entered for everything, I am working to change this to be object oriented and easily changable, you will be able to get these changes in the github links in the main README file

## Contact

Once again, for questions or issues, contact me at:  
**oscarjepsen2007@gmail.com**
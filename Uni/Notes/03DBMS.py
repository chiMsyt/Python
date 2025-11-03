'''
Databas Management System

Definition: Software that interacts with end-users, applications, and the database itself to capture and analyze data.

Core Functions: 
- Create, Read, Update, Delete (CRUD) data.
- Manage database structure (tables, schemas).
- Maintain data security and integrity

Why DBMS with Python?
- Persistence: Data survives after the program ends
- Efficiency: Efficiently handle large amounts of data.
- Concurrency: Manage multiple users / applications.
- Data Integrity: Enforce rules (e.g., no duplicate IDs).
'''

'''
Introduction to SQLite

What is it? 
- A lightweight, serverless, self-contained, SQL database engine

Key Characteristics:
- Serverless: No separate server process to configure or manage. The database is a single file on disk
- Zero Configuration: No setup required. The library is built into Python!
- Cross-Platform: The database file works on any operating system

Ideal Use Cases:
- Prototyping and small to medium-sized applications
- Embedded systems (mobile apps, IoT devices)
- Local caching for larger applications
'''

'''
Connecting Python to SQLite

Python has a built-in module for SQLite: import sqlite3
Basic Workflow:
1. Connect to a database (creates a file if it doesn't exist)
2. Create a Cursor object
3. Execute SQL commands using the cursor
4. Commit the changes
5. Close the connection
'''

# Example:
import sqlite3
conn = sqlite3.connect('mydatabase.db') # connects to a database file named 'mydatabase.db'
cursor = conn.cursor() # creates a cursor object

'''
Creating Tables & Setting Field Properties

What is a table?
- A collection of related data held in a structured format within a database. It consists of rows and columns

SQL Command: CREATE TABLE

Key Components of a Table:
- Table Name: A unique identifier of the table
- Columns / Fields: The different attributes (e.g., id, name, email)
- Data Types: The type of data each column can hold
- Constraints: Rules applied to the data in a column
'''

'''
Common SQLite Data Types and Constraints

Common Data Types:
- INTEGER: Whole numbers (e.g., 1, -5, 100)
- TEXT: String data (e.g., "Hello", "Marsella")
- REAL: Decimal numbers (e.g., 3.14, -0.2)
- NULL: Represents a missing or unknown value

Common Constraints:
- PRIMARY KEY: Unique identifier for each row
- AUTOINCREMENT: Automatically increments the value for new rows (for INTEGER PRIMARY KEY)
- NOT NULL: The column cannot have a NULL value
- UNIQUE: All values in the column must be unique
'''

'''
Summary & Key Takeaways

SQLite is a serverless, file-based DBMS ideal for Python projects
Use the built-in sqlite3 module to interact with it
The core workflow is: 
Connect -> Create Cursor -> Execute SQL -> Commit -> Close
Tables are created using the CREATE TABLE SQL command
Define your table's structure using Data Types and Constraints to ensure data integrity
This foundation allows you to move on to inserting, querying, updating, and deleting data!
'''
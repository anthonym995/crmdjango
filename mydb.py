import mysql.connector
from mysql.connector import Error

try:
    # Connect to the MySQL server
    dataBase = mysql.connector.connect(
        host="localhost",     # Update host if MySQL is not running locally
        user="root",          # Replace with your MySQL username
        password="password123", # Replace with your MySQL password
    )

    if dataBase.is_connected():
        print("Connected to MySQL server")

        # Prepare a cursor object
        cursorObject = dataBase.cursor()

        # Create a database
        cursorObject.execute("CREATE DATABASE IF NOT EXISTS crmdjango")
        print("Database 'crmdjango' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")
finally:
    # Close the connection
    if 'dataBase' in locals() and dataBase.is_connected():
        cursorObject.close()
        dataBase.close()
        print("MySQL connection is closed")

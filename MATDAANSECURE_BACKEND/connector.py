import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # default XAMPP MySQL user
        password="",        # keep empty unless you set a password
        database="votingdb" # your database name
    )

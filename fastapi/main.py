# main.py
from fastapi import FastAPI
import mysql.connector
import os
import time

app = FastAPI()

def get_db_connection():
    attempts = 5
    while attempts > 0:
        try:
            return mysql.connector.connect(
                host=os.getenv("MYSQL_HOST"),
                user=os.getenv("MYSQL_USER"),
                password=os.getenv("MYSQL_PASSWORD"),
                database=os.getenv("MYSQL_DATABASE")
            )
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print("Retrying in 5 seconds...")
            time.sleep(5)
            attempts -= 1
    raise ConnectionError("Unable to connect to the database")

db = get_db_connection()
cursor = db.cursor()

@app.get("/")
def read_root():
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()
    return {"database": db_name}



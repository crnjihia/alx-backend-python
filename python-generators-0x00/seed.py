import mysql.connector
import csv
import uuid

def connect_db():
    return mysql.connector.connect(user='root', password='yourpassword', host='127.0.0.1')

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    connection.commit()
    cursor.close()

def connect_to_prodev():
    return mysql.connector.connect(user='root', password='yourpassword', host='127.0.0.1', database='ALX_prodev')

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_data (
                        user_id VARCHAR(36) PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL,
                        age DECIMAL NOT NULL)''')
    connection.commit()
    cursor.close()

def insert_data(connection, csv_file):
    cursor = connection.cursor()
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                cursor.execute("INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                               (str(uuid.uuid4()), row['name'], row['email'], row['age']))
            except mysql.connector.IntegrityError:
                continue
    connection.commit()
    cursor.close()

"""
    @author: Peter
    @date: 16/08/2024
    @file: initial_db.py
    @description: database schema, create table to initial database
"""
# import mysql.connector
# from constant.db_config import DATABASE_CONFIG
from utils.connect_db import get_connection


# def get_connection():
#     try:
#         connection = mysql.connector.connect(**DATABASE_CONFIG)
#         if connection.is_connected():
#             print('Connecting to MySQL...')
#             return connection
#     except mysql.connector.Error as err:
#         print(err)


def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS admins (
                        user_id VARCHAR(50) PRIMARY KEY,
                        user_name VARCHAR(20) NOT NULL UNIQUE ,
                        password VARCHAR(20) NOT NULL,
                        name VARCHAR(100) NOT NULL,
                        phone VARCHAR(20) NOT NULL UNIQUE ,
                        email VARCHAR(100) NOT NULL UNIQUE,
                        branch_code INT(5) NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                            user_id VARCHAR(50) PRIMARY KEY,
                            user_name VARCHAR(20) NOT NULL UNIQUE ,
                            password VARCHAR(20) NOT NULL,
                            name VARCHAR(100) NOT NULL,
                            license_no VARCHAR(100) NOT NULL UNIQUE,
                            phone VARCHAR(20) NOT NULL UNIQUE
                        )''')
    conn.commit()
    conn.close()

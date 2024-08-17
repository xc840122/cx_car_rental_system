"""
    @author: Peter
    @date: 16/08/2024
    @file: connect_db.py
    @description: encapsulate methods to connect db
"""
from constant.db_config import DATABASE_CONFIG
import mysql.connector


def get_connection():
    try:
        connection = mysql.connector.connect(**DATABASE_CONFIG)
        if connection.is_connected():
            # print('Connected to MySQL...')
            return connection
    except mysql.connector.Error as err:
        print(err)

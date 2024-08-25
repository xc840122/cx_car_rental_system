"""
    @author: Peter
    @date: 16/08/2024
    @file: connect_db.py
    @description: encapsulate methods to connect db
"""
import sqlite3


def get_connection():
    """
    :description: used to connect to the database
    :return: SQLite3 connection object or None if connection fails
    """
    try:
        connection = sqlite3.connect("cx_car_rental.db")
        if connection:
            return connection
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None

"""
    @author: Peter
    @date: 16/08/2024
    @file: customer_login_dao.py
    @description: methods to operate customer login in database
"""
from utils.connect_db import get_connection
from utils.release_db import commit_and_close_connection


def customer_login(user_name: str, password: str):
    """
    Verifies user login by checking the database for matching credentials.

    :param user_name: The username provided by the customer.
    :param password: The password provided by the customer.
    :return: True if login is successful, False otherwise.
    """
    connection = get_connection()
    try:
        cursor = connection.cursor()
        sql = 'SELECT user_id FROM customers WHERE user_name = %s AND password = %s'
        cursor.execute(sql, (user_name, password))
        row = cursor.fetchone()
        return row
    except Exception as e:
        print(f"Error during customer login: {e}")
        return False
    finally:
        commit_and_close_connection(connection)

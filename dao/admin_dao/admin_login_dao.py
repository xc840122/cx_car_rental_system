"""
    @author: Peter
    @date: 16/08/2024
    @file: admin_login_dao.py
    @description: methods to operate login related data in database
"""
from utils.connect_db import get_connection
from utils.release_db import commit_and_close_connection


def admin_login(user_name: str, password: str):
    """
    Verifies admin login by checking the database for matching credentials.

    :param user_name: The username provided by the admin.
    :param password: The password provided by the admin.
    :return: True if login is successful, False otherwise.
    """
    connection = get_connection()
    try:
        cursor = connection.cursor()
        sql = 'SELECT user_id,user_name,password,branch_code FROM admins WHERE user_name = ? AND password = ?'
        cursor.execute(sql, (user_name, password))
        row = cursor.fetchone()
        return row
    except Exception as e:
        print(f"Error during admin login: {e}")
        return False
    finally:
        commit_and_close_connection(connection)

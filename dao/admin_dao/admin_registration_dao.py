"""
    @author: Peter
    @date: 16/08/2024
    @file: admin_registration_dao.py
    @description: methods to operate registration related data in database
"""
from entity.admin import Admin
from utils.connect_db import get_connection
from utils.release_db import commit_and_close_connection


def add_admin(admin: Admin):
    """
    :param admin:
    :return:
    :description: method to add admin_dao to database
    """
    connection = get_connection()
    try:
        cursor = connection.cursor()
        # insert into database
        sql = ('insert into admins (user_id, user_name, '
               'password,branch_code) values (?,?,?,?)')
        value = (admin.user_id, admin.user_name, admin.password, admin.branch_code)
        cursor.execute(sql, value)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        commit_and_close_connection(connection)

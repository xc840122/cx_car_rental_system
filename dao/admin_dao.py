"""
    @author: Peter
    @date: 16/08/2024
    @file: admin_dao.py
    @description: methods to operate admin related data in database
"""
from entity.admin import Admin
from utils.connect_db import get_connection
from utils.release_db import commit_and_close_connection


def add_admin(admin: Admin):
    """
    :param admin:
    :return:
    :description: method to add admin to database
    """
    connection = get_connection()
    cursor = connection.cursor()

    sql = 'insert into admins (user_id, user_name, password,branch_code) values (%s,%s,%s,%s)'
    value = (admin.user_id, admin.user_name, admin.password, admin.branch_code)
    cursor.execute(sql, value)
    commit_and_close_connection(connection)

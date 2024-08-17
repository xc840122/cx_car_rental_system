"""
    @author: Peter
    @date: 16/08/2024
    @file: check_if_duplicated.py
    @description: common tool to check if data is duplicated in db table
"""
from utils.connect_db import get_connection
from utils.release_db import commit_and_close_connection


def check_if_duplicated(table, field, value):
    connection = get_connection()
    cursor = connection.cursor()
    # select from database as value
    sql = f'select * from {table} where {field} = %s;'
    values = (value,)
    cursor.execute(sql, values)
    result = cursor.fetchall()
    commit_and_close_connection(connection)
    return result


# if check_username_in_admins('peter'):
#     print('Username is already in admins')

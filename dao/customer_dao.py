"""
    @author: Peter
    @date: 16/08/2024
    @file: customer_dao.py
    @description: methods to operate customer related data in database
"""

from entity.customer import Customer
from utils.connect_db import get_connection
from utils.release_db import commit_and_close_connection


def add_customer(customer: Customer):
    """
    :param customer:
    :return:
    :description: method to add customer to database
    """
    connection = get_connection()
    cursor = connection.cursor()
    # insert data into database
    sql = 'insert into customers (user_id, user_name, password, name, license_no, phone) values (%s,%s,%s,%s,%s,%s)'
    value = (
    customer.user_id, customer.user_name, customer.password, customer.name, customer.license_no, customer.phone)
    cursor.execute(sql, value)
    commit_and_close_connection(connection)


def customer_login(user_name: str, password: str):
    """
    :description: check database to verify user login
    :param user_name:
    :param password:
    :return:
    """
    connection = get_connection()
    cursor = connection.cursor()
    # select data from database
    sql = 'select * from customers where user_name = %s and password = %s'
    value = (user_name, password)
    cursor.execute(sql, value)
    row = cursor.fetchone()
    if row:
        return True
    else:
        return False


def customer_browse_car():
    pass


def customer_order_car():
    pass


def customer_browse_order():
    pass

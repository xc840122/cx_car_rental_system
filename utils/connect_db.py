"""
    @author: Peter
    @date: 16/08/2024
    @file: connect_db.py
    @description: encapsulate methods to connect db
"""
import mysql.connector

from constant.db_config import SETUP_DATABASE_CONFIG, CREATE_DATABASE_CONFIG


def create_database_connection():
    """
    :description: used to create database
    :return:
    """
    try:
        connection = mysql.connector.connect(**CREATE_DATABASE_CONFIG)
        if connection.is_connected():
            # print('Connected to MySQL...')
            return connection
    except mysql.connector.Error as err:
        print(err)


def get_connection():
    """
    :description: used to connect db
    :return:
    """
    try:
        connection = mysql.connector.connect(**SETUP_DATABASE_CONFIG)
        if connection.is_connected():
            # print('Connected to MySQL...')
            return connection
    except mysql.connector.Error as err:
        print(err)

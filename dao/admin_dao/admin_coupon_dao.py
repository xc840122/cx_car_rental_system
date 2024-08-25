"""
    @author: Peter
    @date: 23/08/2024
    @file: admin_coupon_dao.py
    @description: data logic of coupon, database operation
"""
from typing import List, Union
from utils.connect_db import get_connection
from utils.release_db import commit_and_close_connection


def add_coupons_dao(coupon_list: List):
    """
        :description: Data access layer to add coupon
        :return: List of added coupon
        """
    connection = get_connection()
    cursor = connection.cursor()
    try:
        sql = '''INSERT INTO coupons (
        coupon_id, 
        denomination, 
        description, 
        status, start_date, 
        expired_date, 
        created_at) VALUES (?, ?, ?, ?, ?, ?, ?)'''

        values = coupon_list
        cursor.executemany(sql, values)
        return True
    except Exception as e:
        print(f"Error add coupons: {e}")
        return False
    finally:
        commit_and_close_connection(connection)


def get_coupons_dao(coupon_status: str) -> Union[list, bool]:
    """
    :description: Data access layer to get coupons
    :param: coupon_status
    :return: List of coupons
    """
    connection = get_connection()
    cursor = connection.cursor()
    try:
        sql = '''
        SELECT 
        coupon_id, 
        denomination, 
        description, 
        status, 
        start_date, 
        expired_date, 
        created_at 
        from coupons WHERE status = ?'''

        values = (coupon_status,)
        cursor.execute(sql, values)
        # result from database
        coupon_row_list = cursor.fetchall()
        return coupon_row_list
    except Exception as e:
        print(f"Error get coupons: {e}")
        return False
    finally:
        commit_and_close_connection(connection)


def update_coupons_status_dao(coupon_id, status):
    """
    :description: Data access layer to update coupon
    :param coupon_id:
    :param status:
    :return:
    """
    connection = get_connection()
    cursor = connection.cursor()
    try:
        sql = '''
        UPDATE coupons SET status = ?
        WHERE coupon_id LIKE ?'''

        values = (status, coupon_id)
        cursor.execute(sql, values)
        return True
    except Exception as e:
        print(f"Error update coupons: {e}")
        return False
    finally:
        commit_and_close_connection(connection)

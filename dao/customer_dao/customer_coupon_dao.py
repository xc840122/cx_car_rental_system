"""
    @author: Peter
    @date: 23/08/2024
    @file: customer_coupon_dao.py
    @description: data logic of coupon, database operation
"""

from typing import Union
from entity.coupon import Coupon
from utils.connect_db import get_connection
from utils.release_db import commit_and_close_connection


def verify_coupon_dao(coupon_id: str) -> Union[Coupon, bool]:
    """
    Verify the coupon details from the database using the coupon code.

    :param coupon_id: The coupon code to verify.
    :return: CouponDto if the coupon exists and is valid, otherwise None.
    """
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Query to fetch the coupon details based on the coupon code
        sql = """
        SELECT 
        coupon_id, 
        denomination, 
        description, 
        status, 
        start_date, 
        expired_date,
        created_at 
        FROM coupons WHERE coupon_id = ?"""
        cursor.execute(sql, (coupon_id,))
        row = cursor.fetchone()

        if row:
            # Construct a CouponDto from the database row
            coupon = Coupon(*row)
            return coupon

    except Exception as e:
        print(f"Error verifying coupon: {e}")
        return False
    finally:
        commit_and_close_connection(connection)


def update_coupon_status_dao(coupon_id: str, new_status: str) -> bool:
    """
    Update the status of a coupon in the database.

    :param coupon_id: The ID of the coupon to update.
    :param new_status: The new status to set for the coupon.
    :return: True if the update was successful, False otherwise.
    """
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # SQL query to update the coupon status
        sql = '''UPDATE coupons SET status = ? WHERE coupon_id = ?'''
        cursor.execute(sql, (new_status, coupon_id))
        # Check if any row was affected
        if cursor.rowcount > 0:
            return True

    except Exception as e:
        print(f"Error updating coupon status: {e}")
    finally:
        commit_and_close_connection(connection)

    return False

"""
    @author: Peter
    @date: 20/08/2024
    @file: admin_order_dao.py
    @description: methods to operate order related data in database
"""
from entity.order import Order
from utils.connect_db import get_connection
from utils.release_db import commit_and_close_connection


def get_order_list() -> list[Order]:
    """
    :description: Data access layer to retrieve the list of orders from the database.
    :return: List of Order objects.
    """
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Fetch all orders from the database
        sql = """
        SELECT order_id,
               customer_id,
               car_id,
               rent_start_date,
               rent_end_date,
               total_cost,
               status,
               created_at
               FROM car_rental_orders
               WHERE status = 'PENDING'
               """
        cursor.execute(sql)
        rows = cursor.fetchall()

        # Convert each row to an Order object
        order_list = [Order(*row) for row in rows]

        return order_list
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        commit_and_close_connection(connection)


def approve_order_dao(order_id: str, audit_result: bool) -> bool:
    """
    :description: Data access layer to approve an order in the database.
    :param order_id: The ID of the order to be approved.
    :param audit_result: Boolean value to indicate if the order should be audited or not.
    :return: True if the order is approved successfully, otherwise False.
    """
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Update the status of the order to 'APPROVED'
        if audit_result:
            sql = 'UPDATE car_rental_orders SET status = %s WHERE order_id = %s AND status = %s'
            cursor.execute(sql, ('APPROVED', order_id, 'PENDING'))
        elif not audit_result:
            sql = 'UPDATE car_rental_orders SET status = %s WHERE order_id = %s AND status = %s'
            cursor.execute(sql, ('REJECTED', order_id, 'PENDING'))

        # Check if the update was successful
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        commit_and_close_connection(connection)

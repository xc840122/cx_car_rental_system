"""
    @author: Peter
    @date: 20/08/2024
    @file: customer_order_dao.py
    @description: methods to operate customer order in database
"""
import sqlite3
from datetime import date

from entity.order import Order
from utils.connect_db import get_connection
from utils.release_db import commit_and_close_connection


def customer_car_date_available(car_id: int, start_date: date, end_date: date) -> int:
    """
    :description: Check the database for any conflicting bookings within the specified date range
    :param car_id: ID of the car to check
    :param start_date: Rental start date (YYYY-MM-DD)
    :param end_date: Rental end date (YYYY-MM-DD)
    :return: numbers of search
    """
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Query to check for overlapping bookings
        sql = """
        SELECT COUNT(*)
        FROM car_rental_orders
        WHERE car_id = ?
        AND status IN ('APPROVED', 'PENDING') -- Only check for active or upcoming rentals
        AND (
            (rent_start_date <= ? AND rent_end_date >= ?) -- New start date falls within an existing rental
        OR (rent_start_date <= ? AND rent_end_date >= ?) -- New end date falls within an existing rental
        OR (rent_start_date >= ? AND rent_end_date <= ?) -- Existing rental falls completely within the new rental period
        )
        """
        cursor.execute(sql, (car_id,start_date,start_date,end_date, end_date, start_date,end_date))
        row = cursor.fetchone()
        # If count is 0, the car is available
        return row[0]

    except Exception as e:
        print(f"Error: {e}")

    finally:
        commit_and_close_connection(connection)


def customer_order_car(order: Order):
    """
        :description: Save a new order in the database
        :param order: the order to save
        :return: Boolean indicating success of the order operation
        """
    connection = get_connection()
    cursor = connection.cursor()
    try:
        sql = ('INSERT INTO car_rental_orders ('
               'order_id, '
               'customer_id, '
               'car_id, '
               'coupon_id,'
               'rent_start_date, '
               'rent_end_date,'
               'total_cost) '
               'VALUES (?, ?, ?, ?, ?, ?,?)')
        values = (order.order_id, order.customer_id, order.car_id, order.coupon_id, order.rent_start_date,
                  order.rent_end_date, float(order.total_cost))
        cursor.execute(sql, values)
        return True
    except sqlite3.Error as e:
        print(f"Error booking car: {e}")
        return False
    finally:
        commit_and_close_connection(connection)


def get_customer_orders(customer_id: str) -> list[Order]:
    """
    :param customer_id: ID of the customer
    :return: List of Order objects
    """
    connection = get_connection()
    cursor = connection.cursor()
    try:
        sql = '''
        SELECT 
        order_id, 
        customer_id, 
        car_id, 
        coupon_id,
        rent_start_date, 
        rent_end_date, 
        total_cost, 
        status, 
        created_at
        FROM car_rental_orders
        WHERE customer_id = ?
        '''
        # get all orders of the customer
        cursor.execute(sql, (customer_id,))
        rows = cursor.fetchall()

        order_list = []
        # convert tuple (row) to order object
        for row in rows:
            order = Order(*row)
            # add each order object to list
            order_list.append(order)
        return order_list

    except Exception as e:
        print(f"Error booking car: {e}")
        return []
    finally:
        commit_and_close_connection(connection)

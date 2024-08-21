"""
    @author: Peter
    @date: 20/08/2024
    @file: customer_order_dao.py
    @description: methods to operate customer order in database
"""
from datetime import date

from dto.order_dto import OrderDto
from entity.order import Order
from utils.connect_db import get_connection
from utils.release_db import commit_and_close_connection


def customer_car_date_available(car_id: int, start_date: date, end_date: date) -> bool:
    """
    :description: Check the database for any conflicting bookings within the specified date range
    :param car_id: ID of the car to check
    :param start_date: Rental start date (YYYY-MM-DD)
    :param end_date: Rental end date (YYYY-MM-DD)
    :return: True if the car is available, False otherwise
    """
    connection = get_connection()

    try:
        cursor = connection.cursor()
        # Query to check for overlapping bookings
        sql = """
        SELECT COUNT(*) FROM car_rental_orders 
        WHERE car_id = %s 
        AND (rent_start_date <= %s AND rent_end_date >= %s);
        """
        cursor.execute(sql, (car_id, end_date, start_date))
        row = cursor.fetchone()

        # If count is 0, the car is available
        return row[0] == 0

    except Exception as e:
        print(f"Error: {e}")
        return False

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
               'rent_start_date, '
               'rent_end_date,'
               'total_cost) '
               'VALUES (%s, %s, %s, %s, %s, %s)')
        values = (order.order_id, order.customer_id, order.car_id, order.rent_start_date,
                  order.rent_end_date, order.total_cost)
        cursor.execute(sql, values)
        return True
    except Exception as e:
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
        SELECT order_id, customer_id, car_id, rent_start_date, rent_end_date, total_cost, status, created_at
        FROM car_rental_orders
        WHERE customer_id = %s
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


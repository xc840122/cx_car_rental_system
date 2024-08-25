"""
    @author: Peter
    @date: 18/08/2024
    @file: customer_car_dao.py
    @description: methods to get car data from database
"""
from typing import List, Union
from entity.car import Car
from utils.connect_db import get_connection
from utils.release_db import commit_and_close_connection


def customer_get_car_by_id(car_id: int) -> Union[Car, bool]:
    """
        :description: Retrieves a car's details from the database by its ID.
        :param car_id: The ID of the car to retrieve.
        :return: A Car object if the car is found, None otherwise.
        """
    connection = get_connection()
    cursor = connection.cursor()
    try:
        # SQL query to select the car by ID
        sql = ('SELECT car_id, make, model, year, mileage, available, '
               'unit_price, min_rent_period, max_rent_period '
               'FROM cars WHERE car_id = ? and available = ?')
        cursor.execute(sql, (car_id, 1))
        # Fetch the car data
        row = cursor.fetchone()
        # Create and return a Car object using the retrieved data
        if row:
            car = Car(*row)
            return car

    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        commit_and_close_connection(connection)


def customer_get_cars() -> Union[bool, List[Car]]:
    """
    :description: Retrieves the list of all cars from the database
    :return: List of Car objects
    """
    connection = get_connection()
    try:
        cursor = connection.cursor()

        # Query to select cars which are available from the cars table
        sql = '''SELECT car_id, make, model, year, mileage,available,unit_price,
               min_rent_period, max_rent_period FROM cars where available != ?'''
        values = (0,)
        cursor.execute(sql, values)

        # Fetch all rows from the executed query
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(f"Error during get cars: {e}")
        return False
    finally:
        # Release the resource
        commit_and_close_connection(connection)

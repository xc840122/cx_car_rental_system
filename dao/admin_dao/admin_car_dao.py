"""
    @author: Peter
    @date: 18/08/2024
    @file: admin_car_dao.py
    @description: methods to operate car related data in database
"""
from typing import List, Union

from dto.car_dto import CarDto
from entity.car import Car
from utils.connect_db import get_connection
from utils.release_db import commit_and_close_connection


def add_car(car_dto: CarDto):
    """
    :description: method to add cars to database
    :return:
    """
    connection = get_connection()
    try:
        cursor = connection.cursor()
        # insert car data into database
        sql = ('insert into cars (make, model, year, mileage,unit_price ,min_rent_period,max_rent_period) '
               'values (?,?,?,?,?,?,?);')
        value = (car_dto.make, car_dto.model, car_dto.year, car_dto.mileage,
                 car_dto.unit_price, car_dto.min_rent_period, car_dto.max_rent_period)
        row = cursor.execute(sql, value)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        # release resource
        commit_and_close_connection(connection)


def get_cars() -> Union[List[Car], bool]:
    """
    :description: Retrieves the list of all cars from the database
    :return: List of Car objects
    """
    connection = get_connection()
    try:
        cursor = connection.cursor()
        # Query to select all cars from the cars table
        sql = ('SELECT car_id, make, model, year, mileage,available,'
               'unit_price,min_rent_period, max_rent_period FROM cars')
        cursor.execute(sql)
        # Fetch all rows from the executed query
        rows = cursor.fetchall()
        return rows

    except Exception as e:
        print(f"Error: {e}")
        return False

    finally:
        # Release the resource
        commit_and_close_connection(connection)


def get_car_by_id(car_id: int) -> Union[Car, bool]:
    """
        :description: Retrieves a car's details from the database by its ID.
        :param car_id: The ID of the car to retrieve.
        :return: A Car object if the car is found, None otherwise.
        """
    connection = get_connection()
    # SQL query to select the car by ID
    sql = ('SELECT car_id, make, model, year, mileage, available, '
           'unit_price, min_rent_period, max_rent_period '
           'FROM cars WHERE car_id = ?')
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (car_id,))
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


def update_car(car: Car) -> bool:
    """
    :description: Updates the car information in the database.
    :param car: Car object with updated information.
    :return: True if the update was successful, False otherwise.
    """
    connection = get_connection()

    # SQL query to update the car's information
    sql = (
        'UPDATE cars SET make = ?, model = ?, year = ?, '
        'mileage = ?, available = ?,unit_price=?, '
        'min_rent_period= ?, max_rent_period = ?, '
        'updated_at = CURRENT_TIMESTAMP WHERE car_id = ?'
    )
    values = (
        car.make,
        car.model,
        car.year,
        car.mileage,
        car.available,
        car.unit_price,
        car.min_rent_period,
        car.max_rent_period,
        car.car_id
    )

    try:
        cursor = connection.cursor()
        cursor.execute(sql, values)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        commit_and_close_connection(connection)


def delete_car_by_id(car_id: int) -> bool:
    """
    :description: Deletes a car from the database by its ID.
    :param car_id: ID of the car to be deleted.
    :return: True if the car was successfully deleted, False otherwise.
    """
    connection = get_connection()
    try:
        cursor = connection.cursor()
        sql = 'DELETE FROM cars WHERE car_id = ?'
        cursor.execute(sql, (car_id,))
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        commit_and_close_connection(connection)

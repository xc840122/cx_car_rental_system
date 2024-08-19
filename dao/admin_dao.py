"""
    @author: Peter
    @date: 16/08/2024
    @file: admin_dao.py
    @description: methods to operate admin related data in database
"""
from typing import List

from dto.car_dto import CarDto
from entity.admin import Admin
from entity.car import Car
from utils.connect_db import get_connection
from utils.release_db import commit_and_close_connection


def add_admin(admin: Admin):
    """
    :param admin:
    :return:
    :description: method to add admin to database
    """
    connection = get_connection()
    cursor = connection.cursor()

    sql = 'insert into admins (user_id, user_name, password,branch_code) values (%s,%s,%s,%s)'
    value = (admin.user_id, admin.user_name, admin.password, admin.branch_code)
    cursor.execute(sql, value)
    commit_and_close_connection(connection)


def admin_login(user_name: str, password: str):
    """
    :description: check database to verify user login
    :param user_name:
    :param password:
    :return:
    """
    connection = get_connection()
    cursor = connection.cursor()
    # select data from database
    sql = 'select * from admins where user_name = %s and password = %s'
    value = (user_name, password)
    cursor.execute(sql, value)
    row = cursor.fetchone()
    # release resource
    commit_and_close_connection(connection)
    if row:
        return True
    else:
        return False


def add_car(car_dto: CarDto):
    """
    :description: method to add cars to database
    :return:
    """
    connection = get_connection()
    cursor = connection.cursor()
    # insert car data into database
    sql = ('insert into cars (make, model, year, mileage,unit_price ,min_rent_period,max_rent_period) '
           'values (%s,%s,%s,%s,%s,%s,%s);')
    value = (car_dto.make, car_dto.model, car_dto.year, car_dto.mileage,
             car_dto.unit_price, car_dto.min_rent_period, car_dto.max_rent_period)
    row = cursor.execute(sql, value)
    # release resource
    commit_and_close_connection(connection)
    if row:
        return True
    else:
        return False


def get_cars() -> List[Car]:
    """
    :description: Retrieves the list of all cars from the database
    :return: List of Car objects
    """
    connection = get_connection()
    cursor = connection.cursor()

    # Query to select all cars from the cars table
    sql = ('SELECT car_id, make, model, year, mileage,unit_price,available,'
           'min_rent_period, max_rent_period FROM cars')
    cursor.execute(sql)

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Release the resource
    commit_and_close_connection(connection)

    return rows


def get_car_by_id(car_id: int) -> Car:
    """
        :description: Retrieves a car's details from the database by its ID.
        :param car_id: The ID of the car to retrieve.
        :return: A Car object if the car is found, None otherwise.
        """
    connection = get_connection()
    cursor = connection.cursor()

    # SQL query to select the car by ID
    sql = ('SELECT car_id, make, model, year, mileage, available, '
           'unit_price, min_rent_period, max_rent_period '
           'FROM cars WHERE car_id = %s')
    cursor.execute(sql, (car_id,))

    # Fetch the car data
    row = cursor.fetchone()
    # close session
    commit_and_close_connection(connection)

    if row:
        # Create and return a Car object using the retrieved data
        car = Car(
            car_id=row[0],
            make=row[1],
            model=row[2],
            year=row[3],
            mileage=row[4],
            available=row[5],
            unit_price=row[6],
            min_rent_period=row[7],
            max_rent_period=row[8]
        )
        return car
    else:
        # Return None if no car was found with the given ID
        return None


def update_car(car: Car) -> bool:
    """
    :description: Updates the car information in the database.
    :param car: Car object with updated information.
    :return: True if the update was successful, False otherwise.
    """
    connection = get_connection()
    cursor = connection.cursor()

    # SQL query to update the car's information
    sql = (
        'UPDATE cars SET make = %s, model = %s, year = %s, '
        'mileage = %s, available = %s,unit_price=%s, '
        'min_rent_period= %s, max_rent_period = %s, '
        'updated_at = CURRENT_TIMESTAMP WHERE car_id = %s'
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
        cursor.execute(sql, values)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        commit_and_close_connection(connection)

"""
    @author: Peter
    @date: 18/08/2024
    @file: admin_car_service.py
    @description: car operation logic of admin
"""
from typing import List

from dao.admin_dao.admin_car_dao import add_car, get_cars, get_car_by_id, update_car, delete_car_by_id
from dao.admin_dao.admin_order_dao import get_order_by_car
from dto.car_dto import CarDto
from entity.car import Car
from enum_entity.message import Message


def add_car_service(car_dto: CarDto):
    """
    :param car_dto:
    :return:
    """
    return add_car(car_dto)


def get_car_list_service() -> List[Car]:
    """
    :return: list of cars which information are presented on CUI
    """
    # list of car objects fetched from database
    car_sql_list = get_cars()
    car_obj_list = []
    # iterate the list, transfer car tuple to car object
    for car in car_sql_list:
        car_obj = Car(*car)
        car_obj_list.append(car_obj)

    return car_obj_list


def get_car_by_id_service(car_id: int) -> Car:
    """
    get car by id for admin using
    :param car_id:
    :return:
    """
    current_car = get_car_by_id(car_id)
    return current_car


def modify_car_service(car: Car):
    """
    :description: avoid the null value
    :param car:
    :return:
    """
    # get current value of car
    current_car = get_car_by_id_service(car.car_id)
    # if the value from input is null, replace by current value
    if not car.make:
        car.make = current_car.make
    if not car.model:
        car.model = current_car.model
    if not car.year:
        car.year = current_car.year
    if not car.mileage:
        car.mileage = current_car.mileage
    if not car.available:
        car.available = current_car.available
    if not car.unit_price:
        car.unit_price = current_car.unit_price
    if not car.min_rent_period:
        car.min_rent_period = current_car.min_rent_period
    if not car.max_rent_period:
        car.max_rent_period = current_car.max_rent_period
    # call data layer to update car in database
    return update_car(car)


def delete_car_service(car_id: int) -> bool:
    """
    :description: Handles the logic for deleting a car.
    :param car_id: ID of the car to be deleted.
    :return: True if the car was successfully deleted, False otherwise.
    """
    # verify is there is order related to the car_id
    result = verify_if_car_rented(car_id)
    if result:
        print(Message.CAR_IS_RENTED.value)
        return True
    else:
        delete_car_by_id(car_id)
        return False


def verify_if_car_rented(car_id: int) -> bool:
    """
        :description: Verifies if the car was rented in the car.
        :param car_id:
        :return:
    """
    result = get_order_by_car(car_id)
    if result:
        return True
    else:
        return False

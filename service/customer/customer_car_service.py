"""
    @author: Peter
    @date: 21/08/2024
    @file: customer_car_service.py
    @description: car logic of customer
"""
from typing import List
from dao.customer_dao.customer_car_dao import customer_get_cars, customer_get_car_by_id
from entity.car import Car


def customer_get_car_by_id_service(car_id: int) -> Car:
    """
    get car by car id
    :param car_id:
    :return:
    """
    current_car = customer_get_car_by_id(car_id)
    # transfer the tuple to object
    return current_car


def customer_get_car_list_service() -> List[Car]:
    """
    :return: list of cars which information are presented on customer CUI
    """
    # list of car objects fetched from database
    car_sql_list = customer_get_cars()
    car_obj_list = []
    # iterate the list, transfer car tuple to car object
    for car in car_sql_list:
        car_obj = Car(*car)
        car_obj_list.append(car_obj)
    # filter cars which are available (not hide(0) or rented(2))
    filtered_car_obj_list = [car for car in car_obj_list if car.available != 0]
    return filtered_car_obj_list

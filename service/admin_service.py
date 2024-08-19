"""
    @author: Peter
    @date: 16/08/2024
    @file: admin_service.py
    @description: operations of admin service
"""
from typing import Optional, List

from dto.login_dto import LoginDto
from entity.admin import Admin
from dto.admin_dto import AdminDto
from entity.car import Car
from exception.duplicated_exception import DuplicatedException
from utils.check_if_duplicated import check_if_duplicated
from utils.generate_id import generate_user_id
from dao.admin_dao import add_admin, admin_login, add_car, get_cars, update_car, get_car_by_id
from dto.car_dto import CarDto


def admin_sign_up_service(admin_dto: AdminDto):
    """
    :param admin_dto: get from controller, input by admin
    :return: success str
    """
    # prepare the values of admin
    # uuid to generate unique id
    user_id = generate_user_id()
    user_name = admin_dto.user_name
    password = admin_dto.password
    branch_code = admin_dto.branch_code
    # generate admin object
    admin = Admin(user_id, user_name, password, branch_code)
    # check if unique field 'user_name' is existed or not
    check_username = check_if_duplicated('admins', 'user_name', admin.user_name)
    if check_username:
        raise DuplicatedException("username already exists")
    else:
        # call data layer to save admin info into database
        add_admin(admin)


def admin_login_service(login_dto: LoginDto):
    """
    :param login_dto: include login information
    :return: result of login verification
    """
    user_name = login_dto.user_name
    password = login_dto.password
    return admin_login(user_name, password)


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
    # iterate the list, transfer to car tuple to car object
    for car in car_sql_list:
        car = Car(
            car_id=car[0],
            make=car[1],
            model=car[2],
            year=car[3],
            mileage=car[4],
            unit_price=car[5],
            available=car[6],
            min_rent_period=car[7],
            max_rent_period=car[8]
        )
        car_obj_list.append(car)

    return car_obj_list


def modify_car_service(car: Car):
    """
    :description: avoid the null value
    :param car:
    :return:
    """
    # get current value of car
    current_car = get_car_by_id(car.car_id)
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

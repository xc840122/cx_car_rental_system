"""
    @author: Peter
    @date: 16/08/2024
    @file: admin_controller.py
    @description: interface with user, get input from CUI
"""
from prettytable import PrettyTable

from constant.car_columns import CAR_COLUMNS
from dto.admin_dto import AdminDto
from dto.car_dto import CarDto
from dto.login_dto import LoginDto
from entity.car import Car
from enum_entity.car_make import CarMakeEnum
from enum_entity.car_model import CarModelEnum
from enum_entity.message import Message
from entity.login_cache import LoginCache
from service.admin_service import admin_sign_up_service, admin_login_service, add_car_service, get_car_list_service, \
    modify_car_service, delete_car_service

admin_login_cache = None


def admin_sign_up_controller():
    """
    :description: interface with admins, get input from CUI
    :return:
    """
    user_name = input('Please enter your user name: ')
    password = input('Please enter your password: ')
    branch_code = input('Please enter your branch code: ')
    # pass values to service layer with AdminDto entity
    admin_dto = AdminDto(user_name, password, branch_code)
    admin_sign_up_service(admin_dto)
    return 'success'


def admin_login_controller():
    """
    :description: interface with admin, login from CUI
    :return: result of login
    """
    # ask customer to input user_name and password
    user_name = input('Please enter your username: ')
    password = input('Please enter your password: ')
    # create login_dto object
    login_dto = LoginDto(user_name, password)
    login_result = admin_login_service(login_dto)
    if login_result:
        # cache login information
        admin_login_cache = LoginCache(login_dto)
        print(Message.ADMIN_LOGIN_SUCCESSFUL.value)
        return True
    else:
        print(Message.ADMIN_LOGIN_FAILED.value)
        return False


def add_car_controller():
    """
    :description: interface with admin, add cars to CUI
    :return:
    """
    # input basic information of a car
    car_make = car_make_select()
    car_model = car_model_select()
    car_year = input('Please enter the car year: ')
    car_mileage = input('Please enter the car mileage(KM): ')
    car_unit_price = input('Please enter the car unit price(NZD): ')
    car_min_rent_period = input('Please enter the car min_rent period(DAY): ')
    car_max_rent_period = input('Please enter the car max_rent period(DAY): ')

    # create car object with input
    car_dto = CarDto(car_make, car_model, car_year, car_mileage, car_unit_price,
                     car_min_rent_period, car_max_rent_period)
    # call service layer to add car
    result = add_car_service(car_dto)
    # feedback to admin on CUI
    if result:
        print(Message.ADD_CAR_SUCCESSFUL.value)
        return True
    else:
        print(Message.ADD_CAR_FAILED.value)
        return False


def get_car_list_controller():
    """
    :description: interface with admin, get all cars list from CUI
    :return:
    """
    # Initialize PrettyTable with column names
    table = PrettyTable()
    table.field_names = [
        CAR_COLUMNS["CAR_ID"],
        CAR_COLUMNS["MAKE"],
        CAR_COLUMNS["MODEL"],
        CAR_COLUMNS["YEAR"],
        CAR_COLUMNS["MILEAGE"],
        CAR_COLUMNS["AVAILABLE"],
        CAR_COLUMNS["UNIT_PRICE"],
        CAR_COLUMNS["MIN_RENT_PERIOD"],
        CAR_COLUMNS["MAX_RENT_PERIOD"]
    ]

    # Fetch the car list
    car_list = get_car_list_service()
    # Add rows to the table
    for car in car_list:
        table.add_row([
            car.car_id,
            car.make,
            car.model,
            car.year,
            car.mileage,
            car.available,
            car.unit_price,
            car.min_rent_period,
            car.max_rent_period
        ])

    # Print the formatted table
    print(table)


def modify_car_controller():
    """
    :description: interface with admin, modify cars from CUI
    :return:
    """
    # get car_dto_list
    car_list = get_car_list_service()
    # fetch id from car_dto_list, generate id list of car
    car_id_list = []
    for car in car_list:
        car_id_list.append(car.car_id)
    # Prompt admin to select a car by id
    while True:
        try:
            input_car_id = int(input("Enter the id of the car you want to modify: "))
            if input_car_id < 0:
                print(Message.INVALID_ID.value)
            elif car_id_list.count(input_car_id) < 1:
                print(Message.CAR_NOT_FOUND.value)
            else:
                selected_car_id = input_car_id
                new_make = input("Please enter the new car make: ")
                new_model = input("Please enter the new car model: ")
                new_year = input("Please enter the new car year: ")
                new_mileage = input("Please enter the new car mileage: ")
                new_available = input("Please enter 1 to present, 0 to hide the car(1:Show/0:Hide): ")
                new_unit_price = input("Please enter the new car unit price: ")
                new_min_rent_period = input("Please enter the new car min_rent period: ")
                new_max_rent_period = input("Please enter the new car max_rent period: ")
                # generate car object for updating
                new_car = Car(selected_car_id, new_make, new_model, new_year, new_mileage,
                              new_unit_price, new_min_rent_period, new_max_rent_period, new_available)

                # call service logic
                modify_car_service(new_car)

                break
        except ValueError:
            print(Message.INPUT_VALID_INTEGER)


def delete_car_controller():
    """
    :description: interface with admin, delete car by id from CUI
    :return:
    """
    # get car_list
    car_list = get_car_list_service()
    # fetch id from car_list, generate id list of car
    car_id_list = []
    for car in car_list:
        car_id_list.append(car.car_id)

    # Prompt admin to select a car by id
    while True:
        try:
            input_car_id = int(input("Enter the id of the car you want to delete: "))
            if input_car_id < 0:
                print(Message.INVALID_ID.value)
            elif car_id_list.count(input_car_id) < 1:
                print(Message.CAR_NOT_FOUND.value)
            else:
                # Call the service layer to delete the car
                result = delete_car_service(input_car_id)
                if result:
                    print(Message.DELETE_CAR_SUCCESSFUL.value)
                else:
                    print(Message.DELETE_CAR_FAILED.value)
                break
        except ValueError:
            print(Message.INPUT_VALID_INTEGER)



def get_order_list_controller():
    pass


def order_approve_controller():
    pass


def car_make_select():
    """
    :description: CUI interface to select car make
    :return:
    """
    # Iterate CarMakeEnum to show the whole list
    print('==========Car make list:==========')
    for item in CarMakeEnum:
        print(item.value)

    while True:
        # Ask admin to choose one
        car_make = input('Please choose a car make to input: ').strip().lower()
        # Verify the input by comparing lowercase versions
        if car_make not in [item.value for item in CarMakeEnum]:
            print('Invalid car make. Please try again.')
        else:
            # Return the original case version from the enum
            return car_make


def car_model_select():
    """
        :description: CUI interface to select car model
        :return:
        """
    # Iterate CarMakeEnum to show the whole list
    print('==========Car model list:==========')
    for item in CarModelEnum:
        print(item.value)

    while True:
        # Ask admin to choose one
        car_model = input('Please choose a car model to input: ').strip().lower()
        # Verify the input
        if car_model not in [item.value for item in CarModelEnum]:
            print('Invalid car model. Please try again.')
        else:
            return car_model

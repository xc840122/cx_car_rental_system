"""
    @author: Peter
    @date: 16/08/2024
    @file: customer_controller.py
    @description: interface with customers, get input from CUI
"""
from dto.customer_dto import CustomerDto
from dto.login_dto import LoginDto
from enum_entity.message import Message
from entity.login_cache import LoginCache
from service.customer_service import customer_sign_up_service, customer_login_service

# global variable to cache login information for global use
customer_login_cache = None


def customer_sign_up_controller():
    """
    :description: interface with customer, sign up from CUI
    :return:result of sign up
    """
    user_name = input('Please enter your user name: ')
    password = input('Please enter your password: ')
    name = input('Please enter your name: ')
    license_no = input('Please enter your license number: ')
    phone = input('Please enter your phone number: ')
    # pass values to service layer with CustomerDto entity
    customer_dto = CustomerDto(user_name, password, name, license_no, phone)
    customer_sign_up_service(customer_dto)
    return 'sign up success'


def customer_login_controller():
    """
    :description: interface with customer, login from CUI
    :return: result of login
    """
    # ask customer to input user_name and password
    user_name = input('Please enter your user name: ')
    password = input('Please enter your password: ')
    # create login_dto object
    login_dto = LoginDto(user_name, password)
    login_result = customer_login_service(login_dto)
    if login_result:
        # cache login information
        customer_login_cache = LoginCache(login_dto)
        print(Message.CUSTOMER_LOGIN_SUCCESSFUL.value)
        return True
    else:
        print(Message.CUSTOMER_LOGIN_FAILED.value)
        return False


def get_car_list_controller():
    pass


def order_car_controller():
    pass


def get_order_list_controller():
    pass

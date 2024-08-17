"""
    @author: Peter
    @date: 16/08/2024
    @file: customer_controller.py
    @description: interface with customers, get input from CUI
"""
from dto.customer_dto import CustomerDto
from service.customer_service import customer_sign_up_service


def customer_sign_up_controller():
    """
    :description: interface with customer, get input from CUI
    :return:
    """
    user_name = input('Please enter your user name: ')
    password = input('Please enter your password: ')
    name = input('Please enter your name: ')
    license_no = input('Please enter your license number: ')
    phone = input('Please enter your phone number: ')
    # pass values to service layer with CustomerDto entity
    customer_dto = CustomerDto(user_name, password, name, license_no, phone)
    customer_sign_up_service(customer_dto)
    return 'success'

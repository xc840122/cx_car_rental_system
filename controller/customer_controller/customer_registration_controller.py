"""
    @author: Peter
    @date: 16/08/2024
    @file: customer_registration_controller.py
    @description: interface with customers, get registration input from CUI
"""
from dto.customer_dto import CustomerDto
from enum_entity.message import Message
from service.customer.customer_registration_service import customer_sign_up_service


def customer_sign_up_controller():
    """
    :description: interface with customer, sign up from CUI
    :return:result of sign up
    """
    print("===== Customer Registration =====")
    # ask customer to input user_name and password
    print(f"""
                1.{Message.NOT_EMPTY_USERNAME_OR_PASSWORD.value}
                2.{Message.USERNAME_AND_PASSWORD_LENGTH.value}
                3.{Message.USERNAME_AND_PASSWORD_FORMAT.value}
                """)

    user_name = input("Please enter your user name: ").strip()
    password = input("Please enter your password: ").strip()
    confirm_password = input("Please confirm your password: ").strip()
    name = input('Please enter your name: ').strip()
    license_no = input('Please enter your license number: ').strip()
    phone = input('Please enter your phone number: ').strip()

    # check password input
    if password != confirm_password:
        print(Message.PASSWORD_MISMATCH.value)
        return False
    # pass values to service layer with CustomerDto entity
    customer_dto = CustomerDto(user_name, password, name, license_no, phone)
    result = customer_sign_up_service(customer_dto)
    if result:
        print(Message.REGISTRATION_SUCCESSFUL.value)
        return True
    else:
        print(Message.REGISTRATION_FAILED.value)
        return False

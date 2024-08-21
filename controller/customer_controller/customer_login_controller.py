"""
    @author: Peter
    @date: 16/08/2024
    @file: customer_login_controller.py
    @description: customer login controller
"""
from dto.login_dto import LoginDto
from entity.login_cache import LoginCache
from enum_entity.message import Message
from service.customer.customer_login_service import customer_login_service


def customer_login_controller():
    """
    :description: interface with customer, login from CUI
    :return: result of login
    """
    # cache current login user for other query
    global login_cache
    # ask customer to input user_name and password
    print(f"""
            1.{Message.NOT_EMPTY_USERNAME_OR_PASSWORD.value}
            2.{Message.USERNAME_AND_PASSWORD_LENGTH.value}
            3.{Message.USERNAME_AND_PASSWORD_FORMAT.value}
            """)
    user_name = input('Please enter your user name: ')
    password = input('Please enter your password: ')
    # create login_dto object
    login_dto = LoginDto(user_name, password)
    # call service to verify login info and get user_id response
    login_user_id = customer_login_service(login_dto)
    # get user id
    if login_user_id:
        # cache login information
        login_cache = LoginCache(login_user_id)
        print(Message.CUSTOMER_LOGIN_SUCCESSFUL.value)
        return True
    else:
        print(Message.CUSTOMER_LOGIN_FAILED.value)
        return False


def current_login_customer() -> str:
    """
    :description: cache and provide current login user info
    :return:
    """
    return login_cache.login_user

"""
    @author: Peter
    @date: 16/08/2024
    @file: admin__login_controller.py
    @description: CUI for admin login
"""
from dto.login_dto import LoginDto
from enum_entity.message import Message
from service.admin.admin_login_service import admin_login_service


def admin_login_controller():
    """
    :description: interface with admin_dao, login from CUI
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
        print(Message.ADMIN_LOGIN_SUCCESSFUL.value)
        return True
    else:
        print(Message.ADMIN_LOGIN_FAILED.value)
        return False
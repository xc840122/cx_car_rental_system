"""
    @author: Peter
    @date: 16/08/2024
    @file: admin_login_service.py
    @description: admin login logic
"""
from dao.admin_dao.admin_login_dao import admin_login
from dto.login_dto import LoginDto


def admin_login_service(login_dto: LoginDto):
    """
    :param login_dto: include login information
    :return: result of login verification
    """
    user_name = login_dto.user_name
    password = login_dto.password
    return admin_login(user_name, password)

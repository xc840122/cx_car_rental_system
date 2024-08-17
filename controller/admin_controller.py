"""
    @author: Peter
    @date: 16/08/2024
    @file: admin_controller.py
    @description: interface with user, get input from CUI
"""
from dto.admin_dto import AdminDto
from service.admin_service import admin_sign_up_service


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

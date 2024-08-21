"""
    @author: Peter
    @date: 16/08/2024
    @file: admin_registration_controller.py
    @description: registration controller for admin
"""
from dto.admin_dto import AdminDto
from enum_entity.message import Message
from service.admin.admin_registration_service import admin_sign_up_service


def admin_sign_up_controller():
    """
    :description: interface with admins, get input from CUI
    :return:
    """
    print("===== Customer Registration =====")
    user_name = input("Please enter your user name: ").strip()
    password = input("Please enter your password: ").strip()
    confirm_password = input("Please confirm your password: ").strip()
    branch_code = input('Please enter your branch code: ').strip()

    # check password input
    if password != confirm_password:
        print(Message.PASSWORD_MISMATCH.value)
        return False
    # pass values to service layer with AdminDto entity
    admin_dto = AdminDto(user_name, password, branch_code)
    result = admin_sign_up_service(admin_dto)
    if result:
        print(Message.REGISTRATION_SUCCESSFUL.value)
        return True
    else:
        print(Message.REGISTRATION_FAILED.value)
        return False

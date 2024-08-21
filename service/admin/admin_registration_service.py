"""
    @author: Peter
    @date: 16/08/2024
    @file: admin_service.py
    @description: admin registration logic
"""
from dao.admin_dao.admin_registration_dao import add_admin
from dto.admin_dto import AdminDto
from entity.admin import Admin
from enum_entity.message import Message
from exception.duplicated_exception import DuplicatedException
from utils.check_if_duplicated import check_if_duplicated
from utils.generate_id import generate_user_id


def admin_sign_up_service(admin_dto: AdminDto):
    """
    :param admin_dto: get from controller, input by admin_dao
    :return: success str
    """
    # prepare the values of admin_dao
    # uuid to generate unique id
    user_id = generate_user_id()
    user_name = admin_dto.user_name
    password = admin_dto.password
    branch_code = admin_dto.branch_code
    # generate admin_dao object
    admin = Admin(user_id, user_name, password, branch_code)
    # check if unique field 'user_name' is existed or not
    check_username = check_if_duplicated('admins', 'user_name', admin.user_name)
    if check_username:
        print(Message.USERNAME_ALREADY_EXISTS.value)
        return False
    else:
        # call data layer to save admin_dao info into database
        return add_admin(admin)



"""
    @author: Peter
    @date: 16/08/2024
    @file: admin_service.py
    @description: operations of admin service
"""
from entity.admin import Admin
from dto.admin_dto import AdminDto
from exception.duplicated_exception import DuplicatedException
from utils.check_if_duplicated import check_if_duplicated
from utils.generate_user_id import generate_user_id
from dao.admin_dao import add_admin


def admin_sign_up_service(admin_dto: AdminDto):
    """
    :param admin_dto: get from controller, input by admin
    :return: success str
    """
    # prepare the values of admin
    # uuid to generate unique id
    user_id = generate_user_id()
    user_name = admin_dto.user_name
    password = admin_dto.password
    branch_code = admin_dto.branch_code
    # generate admin object
    admin = Admin(user_id, user_name, password, branch_code)
    # check if unique field 'user_name' is existed or not
    check_username = check_if_duplicated('admins', 'user_name', admin.user_name)
    if check_username:
        raise DuplicatedException("username already exists")
    else:
        # call data layer to save admin info into database
        add_admin(admin)

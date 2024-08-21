"""
    @author: Peter
    @date: 16/08/2024
    @file: customer_login_service.py
    @description: login logic of customer
"""
from dao.customer_dao.customer_login_dao import customer_login
from dto.login_dto import LoginDto
from enum_entity.message import Message


def customer_login_service(login_dto: LoginDto):
    """
    Verifies the login information provided by the customer.

    :param login_dto: Data Transfer Object that includes login information (username and password).
    :return: True if login is successful, False otherwise.
    """
    user_name = login_dto.user_name.strip()
    password = login_dto.password.strip()

    # Verification checks
    if not user_name or not password:
        print(Message.NOT_EMPTY_USERNAME_OR_PASSWORD)
        return False

    if len(user_name) < 3 or len(password) < 6:
        print(Message.USERNAME_AND_PASSWORD_LENGTH)
        return False

    if "@" in user_name or " " in user_name:
        print(Message.USERNAME_AND_PASSWORD_FORMAT)
        return False

    # If verification passes, attempt login
    row = customer_login(user_name, password)

    # get user id from response tuple
    if row:
        user_id = row[0]
        return user_id
    else:
        return False

"""
    @author: Peter
    @date: 16/08/2024
    @file: customer_registration_service.py
    @description: handle registration logic
"""
from dao.customer_dao.customer_registration_dao import add_customer
from dto.customer_dto import CustomerDto
from entity.customer import Customer
from enum_entity.message import Message
from exception.duplicated_exception import DuplicatedException
from utils.check_if_duplicated import check_if_duplicated
from utils.generate_id import generate_user_id


def customer_sign_up_service(customer_dto: CustomerDto):
    """
    :param customer_dto: get data from controller, input by customer
    :return: success str
    """
    # prepare the values of admin_dao
    # uuid to generate unique id
    user_id = generate_user_id()
    user_name = customer_dto.user_name
    password = customer_dto.password
    name = customer_dto.name
    license_no = customer_dto.license_no
    phone = customer_dto.phone

    # basic Verification checks
    if not (user_name and password):
        print(Message.NOT_EMPTY_USERNAME_OR_PASSWORD.value)
        return False

    if len(user_name) < 3 or len(password) < 6:
        print(Message.USERNAME_AND_PASSWORD_LENGTH.value)
        return False

    if "@" in user_name or " " in user_name:
        print(Message.USERNAME_AND_PASSWORD_FORMAT.value)
        return False

    # generate customer object
    customer = Customer(user_id, user_name, password, name, license_no, phone)
    # check if unique data is already existed
    # check if unique field 'user_name' is existed or not
    check_username = check_if_duplicated('customers', 'user_name', customer.user_name)
    check_license_no = check_if_duplicated('customers', 'license_no', customer.license_no)
    check_phone = check_if_duplicated('customers', 'phone', customer.phone)
    if check_username:
        print(Message.USERNAME_ALREADY_EXISTS.value)
        return False
    elif check_license_no:
        print(Message.LICENSE_NO_ALREADY_EXISTS.value)
        return False
    elif check_phone:
        print(Message.PHONE_ALREADY_EXISTS.value)
        return False
    else:
        # use data layer to insert customer info into database
        return add_customer(customer)

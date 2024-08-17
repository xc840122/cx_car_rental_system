"""
    @author: Peter
    @date: 16/08/2024
    @file: customer_service.py
    @description: operations of customer
"""
from dto.customer_dto import CustomerDto
from entity.customer import Customer
from exception.duplicated_exception import DuplicatedException
from utils.generate_user_id import generate_user_id
from utils.check_if_duplicated import check_if_duplicated
from dao.customer_dao import add_customer


def customer_sign_up_service(customer_dto: CustomerDto):
    """
    :param customer_dto: get data from controller, input by customer
    :return: success str
    """
    # prepare the values of admin
    # uuid to generate unique id
    user_id = generate_user_id()
    user_name = customer_dto.user_name
    password = customer_dto.password
    name = customer_dto.name
    license_no = customer_dto.license_no
    phone = customer_dto.phone
    # generate customer object
    customer = Customer(user_id, user_name, password, name, license_no, phone)
    # check if unique data is already existed
    # check if unique field 'user_name' is existed or not
    check_username = check_if_duplicated('customers', 'user_name', customer.user_name)
    check_license_no = check_if_duplicated('customers', 'license_no', customer.license_no)
    check_phone = check_if_duplicated('customers', 'phone', customer.phone)
    if check_username:
        raise DuplicatedException("user_name already exists")
    elif check_license_no:
        raise DuplicatedException("license_no already exists")
    elif check_phone:
        raise DuplicatedException("phone already exists")
    else:
        # use data layer to insert customer info into database
        add_customer(customer)

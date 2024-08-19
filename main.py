"""
    @author: Peter
    @date: 16/08/2024
    @file: main.py
    @description: cx car rental system, a CUI app to support user registration,
    user login, car management and order management
"""
from controller.customer_controller import customer_sign_up_controller, customer_login_controller
from schema.initial_db import setup_database
from controller.admin_controller import admin_sign_up_controller, admin_login_controller, add_car_controller, \
    get_car_list_controller, modify_car_controller, delete_car_controller


def main():
    # initial database, create tables
    setup_database()
    # admin_sign_up_controller()
    # customer_sign_up_controller()
    # customer_login_controller()
    # admin_login_controller()
    # add_car_controller()
    get_car_list_controller()
    # modify_car_controller()
    delete_car_controller()


if __name__ == "__main__":
    main()

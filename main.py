"""
    @author: Peter
    @date: 16/08/2024
    @file: main.py
    @description: cx car rental system, a CUI app to support user registration,
    user login, car management and order management
"""
from controller.customer_controller import customer_sign_up_controller
from schema.initial_db import setup_database
from controller.admin_controller import admin_sign_up_controller


def main():
    # initial database, create tables
    setup_database()
    # admin_sign_up_controller()
    customer_sign_up_controller()


if __name__ == "__main__":
    main()

"""
    @author: Peter
    @date: 16/08/2024
    @file: main.py
    @description: cx car rental system, a CUI app to support user registration,
    user login, car management and order management
"""
from controller.admin_controller.admin_coupon_controller import add_coupons_controller, get_coupons_controller
from menu.main_menu import main_menu
from schema import initial_db
from schema.initial_db import setup_database


def main():
    setup_database()
    main_menu()


if __name__ == "__main__":
    main()

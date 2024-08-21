"""
    @author: Peter
    @date: 20/08/2024
    @file: admin__menu_controller.py
    @description: menu for admin use
"""
from controller.admin_controller.admin_car_controller import add_car_controller, modify_car_controller, delete_car_controller, \
    get_car_list_controller
from controller.admin_controller.admin_order_controller import get_order_list_controller, order_approve_controller
from enum_entity.message import Message


def admin_menu():
    while True:
        print("\n=== Admin Menu ===")
        print("1. Add Car")
        print("2. Modify Car")
        print("3. Delete Car")
        print("4. Get Car List")
        print("5. Get Order List")
        print("6. Audit Order")
        print("7. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_car_controller()
        elif choice == "2":
            modify_car_controller()
        elif choice == "3":
            delete_car_controller()
        elif choice == "4":
            get_car_list_controller()
        elif choice == "5":
            get_order_list_controller()
        elif choice == "6":
            order_approve_controller()
        elif choice == "7":
            print(Message.LOG_OUT.value)
            break
        else:
            print(Message.INVALID_CHOICE.value)

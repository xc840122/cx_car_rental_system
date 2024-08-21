"""
    @author: Peter
    @date: 20/08/2024
    @file: customer_menu_controller.py
    @description: customer menu
"""
from controller.admin_controller.admin_car_controller import get_car_list_controller
from controller.customer_controller.customer_car_controller import customer_get_car_list_controller
from controller.customer_controller.customer_order_controller import customer_order_car_controller, \
    get_customer_orders_controller
from enum_entity.message import Message


def customer_menu():
    while True:
        print("\n=== Customer Menu ===")
        # Assuming there are controllers for the following operations
        print("1. View Cars")
        print("2. Make an Order")
        print("3. View My Orders")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            customer_get_car_list_controller()
        elif choice == "2":
            customer_order_car_controller()
        elif choice == "3":
            get_customer_orders_controller()
        elif choice == "4":
            print(Message.LOG_OUT.value)
            break
        else:
            print(Message.INVALID_CHOICE.value)

"""
    @author: Peter
    @date: 22/08/2024
    @file: customer_menu.py
    @description: menu for customer
"""
from abstract_entity.menu import Menu
from controller.customer_controller.customer_car_controller import customer_get_car_list_controller
from controller.customer_controller.customer_order_controller import customer_order_car_controller, \
    get_customer_orders_controller
from enum_entity.message import Message


class CustomerMenu(Menu):
    def display(self):
        while True:
            print("\n=== Customer Menu ===")
            # options
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

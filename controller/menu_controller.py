"""
    @author: Peter
    @date: 18/08/2024
    @file: customer_menu_controller.py
    @description: main menu of CUI for both admin_dao and customer use
"""
from controller.admin_controller.admin_login_controller import admin_login_controller
from controller.admin_controller.admin_menu_controller import admin_menu
from controller.admin_controller.admin_registration_controller import admin_sign_up_controller
from controller.customer_controller.customer_login_controller import customer_login_controller
from controller.customer_controller.customer_menu_controller import customer_menu
from controller.customer_controller.customer_registration_controller import customer_sign_up_controller
from enum_entity.message import Message


def main_menu():
    while True:
        print("\n===== Main Menu =====")
        print("1. Admin Sign up")
        print("2. Admin Login")
        print("3. Customer Sign up")
        print("4. Customer Login")
        print("5. Exit")

        choice = input("Please choose an option: ")

        if choice == "1":
            if admin_sign_up_controller():
                main_menu()
        elif choice == "2":
            if admin_login_controller():
                admin_menu()
        elif choice == "3":
            if customer_sign_up_controller():
                main_menu()
        elif choice == "4":
            if customer_login_controller():
                customer_menu()
        elif choice == "5":
            print(Message.EXIT_SYSTEM.value)
            break
        else:
            print(Message.INVALID_CHOICE.value)

"""
    @author: Peter
    @date: 18/08/2024
    @file: customer_menu_controller.py
    @description: main menu of CUI for both admin_dao and customer use
"""
from abstract_entity.user import User
from controller.admin_controller.admin_login_controller import admin_login_controller
from controller.admin_controller.admin_registration_controller import admin_sign_up_controller
from controller.customer_controller.customer_login_controller import customer_login_controller
from controller.customer_controller.customer_registration_controller import customer_sign_up_controller
from entity.admin import Admin
from menu.admin_menu import AdminMenu
from entity.customer import Customer
from menu.customer_menu import CustomerMenu
from enum_entity.message import Message
from menu.decorator.head_foot_decorator import HeaderFooterDecorator


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
            login_admin = admin_login_controller()
            if login_admin:
                sub_menu(login_admin)
        elif choice == "3":
            if customer_sign_up_controller():
                main_menu()
        elif choice == "4":
            login_customer = customer_login_controller()
            if login_customer:
                sub_menu(login_customer)
        elif choice == "5":
            print(Message.EXIT_SYSTEM.value)
            break
        else:
            print(Message.INVALID_CHOICE.value)


# show different sub_menu according to admin/customer role
def sub_menu(user: User):
    if type(user) is Admin:
        admin_sub_menu = AdminMenu()
        HeaderFooterDecorator(admin_sub_menu).display()
    elif type(user) is Customer:
        customer_sub_menu = CustomerMenu()
        HeaderFooterDecorator(customer_sub_menu).display()
    else:
        print("Invalid user role.")
        return

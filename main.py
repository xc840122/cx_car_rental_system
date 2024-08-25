"""
    @author: Peter
    @date: 16/08/2024
    @file: main.py
    @description: cx car rental system, a CUI app to support user registration,
    user login, car management and order management
"""
from menu.main_menu import main_menu
from schema.initial_db import setup_database


def main():
    setup_database()
    main_menu()


if __name__ == "__main__":
    main()

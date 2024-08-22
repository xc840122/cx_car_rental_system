"""
    @author: Peter
    @date: 22/08/2024
    @file: base_menu_decorator.py
    @description: base decorator,enhance the menu with additional function
"""
from abstract_entity.menu import Menu


class BaseMenuDecorator(Menu):
    def __init__(self, decorated_menu):
        self._decorated_menu = decorated_menu

    # the basic function from decorated object
    def display(self):
        self._decorated_menu.display()

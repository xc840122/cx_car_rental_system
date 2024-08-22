"""
    @author: Peter
    @date: 22/08/2024
    @file: menu.py
    @description: abstract base class for menu
"""
from abc import ABC, abstractmethod


class Menu(ABC):
    def display(self):
        pass

"""
    @author: Peter
    @date: 22/08/2024
    @file: base_menu_decorator.py
    @description: apply decorator design mode to add header
    and footer with additional function
"""

from menu.decorator.base_menu_decorator import BaseMenuDecorator


class HeaderFooterDecorator(BaseMenuDecorator):
    # use decorator design mode to extend footer and header
    def display(self):
        print("###############################################")
        print("#                                             #")
        print("#             WELCOME TO CX CAR RENTAL        #")
        print("#                 Customer Matters            #")
        print("#                Contact:0273456789           #")
        print("#                                             #")
        print("###############################################")
        super().display()

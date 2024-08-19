"""
    @author: Peter
    @date: 16/08/2024
    @file: customer_dto.py
    @description: CustomerDto object for transmission of customer sign up
"""


class CustomerDto:
    def __init__(self, user_name, password, name, license_no, phone):
        self.user_name = user_name
        self.password = password
        self.name = name
        self.license_no = license_no
        self.phone = phone

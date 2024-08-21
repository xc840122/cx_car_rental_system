"""
    @author: Peter
    @date: 16/08/2024
    @file: admin_dto.py
    @description: AdminDto object for transmission of admin_dao sign up
"""


class AdminDto:

    def __init__(self, user_name, password,branch_code):
        self.user_name = user_name
        self.password = password
        self.branch_code = branch_code

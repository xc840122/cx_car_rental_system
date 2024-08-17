"""
    @author: Peter
    @date: 16/08/2024
    @file: admin_dto.py
    @description: AdminDto entity for data transmission between controller and service
"""


class AdminDto:

    def __init__(self, user_name, password,branch_code):
        self.user_name = user_name
        self.password = password
        self.branch_code = branch_code

"""
    @author: Peter
    @date: 18/08/2024
    @file: login_cache.py
    @description: cache present login user (admin/customer) for other function using
"""
from dto.login_dto import LoginDto


class LoginCache:
    def __init__(self, login_dto: LoginDto):
        self.login_dto = login_dto

    def get_login_user(self):
        return self.login_dto

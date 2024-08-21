"""
    @author: Peter
    @date: 18/08/2024
    @file: login_cache.py
    @description: cache present login user (admin_dao/customer) for other function using
"""


class LoginCache:
    def __init__(self, user_id: str):
        self.__user_id = user_id

    @property
    def login_user(self):
        return self.__user_id

    @login_user.setter
    def login_user(self, value):
        self.__user_id = value

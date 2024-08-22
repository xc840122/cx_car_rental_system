"""
    @author: Peter
    @date: 18/08/2024
    @file: login_cache.py
    @description: cache present login user (admin_dao/customer) for other function using
"""
from abstract_entity.user import User


class LoginCache:
    def __init__(self, user: User):
        self.__user = user

    @property
    def login_user(self):
        return self.__user

    @login_user.setter
    def login_user(self, value):
        self.__user = value

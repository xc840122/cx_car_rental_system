"""
    @author: Peter
    @date: 16/08/2024
    @file: user.py
    @description: abstract base class for user entity
"""
from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, user_id, user_name, password):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password

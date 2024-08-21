"""
    @author: Peter
    @date: 18/08/2024
    @file: login_dto.py
    @description: LoginDto object for login information transmission
"""


class LoginDto:
    def __init__(self, user_name, password):
        self.__user_name = user_name
        self.__password = password

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    def get_user_name(self):
        """
        :description: Get user_name (encapsulated in a string)
        :return: user_name
        """
        return self.user_name

    def get_password(self):
        """
            :description: Get password (encapsulated in a string)
            :return: password
        """
        return self.password

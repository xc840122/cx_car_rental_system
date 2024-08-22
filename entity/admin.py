"""
    @author: Peter
    @date: 16/08/2024
    @file: admin_dao.py
    @description: Admin entity which is inherited from user
"""
from abstract_entity.user import User


class Admin(User):
    branch_code = None

    def __init__(self, user_id, user_name, password, branch_code):
        super().__init__(user_id, user_name, password)
        self.branch_code = branch_code

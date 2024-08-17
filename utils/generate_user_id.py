"""
    @author: Peter
    @date: 16/08/2024
    @file: generate_user_id.py
    @description: tool to generate random user id
"""
import uuid


def generate_user_id():
    """
    :return: random user id
    """
    return str(uuid.uuid4())

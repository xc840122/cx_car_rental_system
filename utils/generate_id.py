"""
    @author: Peter
    @date: 16/08/2024
    @file: generate_id.py
    @description: tool to generate random id for data storage
"""
import uuid


def generate_user_id():
    """
    :return: random user id
    """
    return str(uuid.uuid4())


def generate_order_id():
    """
    :return: random user id
    """
    return str(f'order-{uuid.uuid4()}')

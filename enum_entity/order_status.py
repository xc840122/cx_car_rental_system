"""
    @author: Peter
    @date: 23/08/2024
    @file: order_status.py
    @description: enum of order status
"""

from enum import Enum


class OrderStatus(Enum):
    PENDING: str = 'PENDING'
    APPROVED: str = 'APPROVED'
    REJECTED: str = 'REJECTED'
    COMPLETED: str = 'COMPLETED'

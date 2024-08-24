"""
    @author: Peter
    @date: 18/08/2024
    @file: coupon_status.py
    @description: enum of coupon status
"""

from enum import Enum


class CouponStatus(Enum):
    PENDING: str = 'PENDING'
    ACTIVATED: str = 'ACTIVATED'
    USED: str = 'USED'
    EXPIRED: str = 'EXPIRED'

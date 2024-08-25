"""
    @author: Peter
    @date: 23/08/2024
    @file: coupon_dto.py
    @description: coupon dto, for transmission need
"""
from datetime import date


class CouponDto:
    def __init__(self,
                 denomination,
                 description,
                 status,
                 start_date,
                 expired_date
                 ):
        self.denomination: float = denomination
        self.description = description
        self.status: str = status
        self.start_date: date = start_date
        self.expired_date: date = expired_date

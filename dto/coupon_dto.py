"""
    @author: Peter
    @date: 23/08/2024
    @file: coupon_dto.py
    @description: coupon dto, for transmission need
"""
from datetime import date
from decimal import Decimal

from enum_entity.coupon_status import CouponStatus


class CouponDto:
    def __init__(self,
                 denomination: Decimal,
                 description,
                 status: str,
                 start_date: date,
                 expired_date: date
                 ):
        self.denomination = denomination
        self.description = description
        self.status = status
        self.start_date = start_date
        self.expired_date = expired_date

"""
    @author: Peter
    @date: 23/08/2024
    @file: coupon.py
    @description: Coupon entity
"""
from datetime import datetime, date
from decimal import Decimal

from enum_entity.coupon_status import CouponStatus


class Coupon:
    def __init__(self,
                 coupon_id: str,
                 denomination: Decimal,
                 description,
                 status: str,
                 start_date: date,
                 expired_date: date,
                 created_at: datetime):
        self.coupon_id = coupon_id
        self.denomination = denomination
        self.description = description
        self.status = status
        self.start_date = start_date
        self.expired_date = expired_date
        self.created_at = created_at or datetime.now()

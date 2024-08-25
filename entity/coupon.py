"""
    @author: Peter
    @date: 23/08/2024
    @file: coupon.py
    @description: Coupon entity
"""
from datetime import datetime, date


class Coupon:
    def __init__(self,
                 coupon_id,
                 denomination,
                 description,
                 status,
                 start_date,
                 expired_date,
                 created_at: datetime):
        self.coupon_id: str = coupon_id
        self.denomination: float = denomination
        self.description = description
        self.status: str = status
        self.start_date = start_date
        self.expired_date = expired_date
        self.created_at: datetime = created_at or datetime.now()

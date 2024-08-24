"""
    @author: Peter
    @date: 23/08/2024
    @file: customer_coupon_service.py
    @description: customer service logic of coupon
"""

from typing import Union
from dao.customer_dao.customer_coupon_dao import verify_coupon_dao, update_coupon_status_dao
from entity.coupon import Coupon
from enum_entity.coupon_status import CouponStatus
from enum_entity.message import Message


def verify_coupon_service(coupon_id: str) -> Union[Coupon, bool]:
    """
    Service layer function to verify the coupon.

    :param coupon_id: The coupon id to verify.
    :return: CouponDto if the coupon exists and is valid, otherwise False.
    """
    # Retrieve coupon details from the DAO layer
    coupon = verify_coupon_dao(coupon_id)

    if coupon:
        return coupon
    else:
        return False


def update_coupon_status_service(coupon_id: str, new_status: str) -> bool:
    """
    Service layer function to update the status of a coupon.

    :param coupon_id: The ID of the coupon to update.
    :param new_status: The new status to set for the coupon.
    :return: True if the update was successful, False otherwise.
    """
    # Validate new status against defined coupon statuses
    if new_status not in [status.value for status in CouponStatus]:
        print(Message.INVALID_COUPON_STATUS.value)
        return False

    # Call the DAO function to update the coupon status in the database
    return update_coupon_status_dao(coupon_id, new_status)


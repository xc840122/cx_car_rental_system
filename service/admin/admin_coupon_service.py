"""
    @author: Peter
    @date: 23/08/2024
    @file: admin_coupon_service.py
    @description: service logic of coupon
"""
from datetime import datetime
from typing import Union

from dao.admin_dao.admin_coupon_dao import add_coupons_dao, get_coupons_dao, update_coupons_status_dao
from dto.coupon_dto import CouponDto
from entity.coupon import Coupon
from utils.generate_id import generate_coupon_id


def add_coupons_service(coupon_dto: CouponDto, coupon_numbers) -> bool:
    """
    :description: add batch of coupons by admin
    :param coupon_dto:
    :param coupon_numbers:
    :return:
    """
    # prepare data from coupon_dto
    denomination = coupon_dto.denomination
    description = coupon_dto.description
    status = coupon_dto.status
    start_date = coupon_dto.start_date
    expired_date = coupon_dto.expired_date

    # create at
    create_at = datetime.now()

    # result_list
    coupon_list = []
    # generate coupon list according to numbers
    while coupon_numbers > 0:
        # generate unique id
        coupon_id = generate_coupon_id()
        # generate coupon object
        coupon_tuple = (coupon_id,
                        denomination,
                        description,
                        status,
                        start_date,
                        expired_date,
                        create_at)
        # add coupon tuple into list
        coupon_list.append(coupon_tuple)
        coupon_numbers -= 1
    # call dao to do batch insert to improve performance
    result = add_coupons_dao(coupon_list)

    if result:
        return True
    else:
        return False


def get_coupons_service(coupon_status: str) -> Union[list[Coupon], bool]:
    """
    :description: get coupons by status
    :param coupon_status:
    :return:
    """
    # list of Coupon object
    list_coupons = []

    # result from database
    list_row_tuple = get_coupons_dao(coupon_status)

    # iterate the list, converse to coupon object
    for coupon_tuple in list_row_tuple:
        coupon = Coupon(*coupon_tuple)
        list_coupons.append(coupon)

    if list_coupons:
        return list_coupons
    else:
        return False


def reset_coupons_status(coupon_id, status) -> bool:
    """
    :description: reset coupon status after rejecting the order
    :param coupon_id:
    :param status:
    :return:
    """
    if update_coupons_status_dao(coupon_id, status):
        return True
    else:
        return False

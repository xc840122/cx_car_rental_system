"""
    @author: Peter
    @date: 24/08/2024
    @file: admin_order_service.py
    @description: admin order service
"""
from dao.admin_dao.admin_order_dao import approve_order_dao, get_order_list, get_order_by_id
from entity.order import Order
from enum_entity.coupon_status import CouponStatus
from service.admin.admin_coupon_service import reset_coupons_status


def approve_order_service(order_id: str, audit_result: bool) -> bool:
    """
    :description: Service layer to handle the approval of an order.
    :param order_id: The ID of the order to be approved.
    :param audit_result: True to audit the approval of the order, False otherwise.
    :return: result if the order is approved successfully, otherwise False.
    """
    # get pending order by id
    pending_order = admin_get_order_by_id(order_id)
    if (not audit_result) and pending_order.coupon_id:
        # reset coupon status to be activated if there is
        reset_coupons_status(pending_order.coupon_id, CouponStatus.ACTIVATED.value)
    # pass to dao to handle
    result = approve_order_dao(order_id, audit_result)
    if result:
        return result
    else:
        return False


def get_order_list_service() -> list[Order]:
    """
    :description: Service layer to fetch the list of orders.
    :return: List of Order objects.
    """
    # Fetch the order list from the DAO layer
    order_list = get_order_list()

    return order_list


def admin_get_order_by_id(order_id: str) -> Order:
    """
    :description: Service layer to fetch the order by id.
    :param order_id:
    :return:
    """
    # Fetch the order by id
    order = get_order_by_id(order_id)
    return order

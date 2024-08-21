"""
    @author: Peter
    @date: 18/08/2024
    @file: admin_order_service.py
    @description: admin order service
"""
from dao.admin_dao.admin_order_dao import approve_order_dao, get_order_list
from entity.order import Order
from enum_entity.message import Message


def approve_order_service(order_id: str, audit_result: bool) -> bool:
    """
    :description: Service layer to handle the approval of an order.
    :param order_id: The ID of the order to be approved.
    :param audit_result: True to audit the approval of the order, False otherwise.
    :return: True if the order is approved successfully, otherwise False.
    """
    # Verify that the order_id is valid and exists in the system
    if not isinstance(order_id, str):
        print(Message.INVALID_ORDER_ID.value)
        return False

    # Call DAO layer to approve the order in the database
    result = approve_order_dao(order_id, audit_result)
    return result


def get_order_list_service() -> list[Order]:
    """
    :description: Service layer to fetch the list of orders.
    :return: List of Order objects.
    """
    # Fetch the order list from the DAO layer
    order_list = get_order_list()

    return order_list

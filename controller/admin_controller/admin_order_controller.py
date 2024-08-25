"""
    @author: Peter
    @date: 20/08/2024
    @file: admin__order_controller.py
    @description: order controller for admin
"""
from prettytable import PrettyTable

from enum_entity.message import Message
from service.admin.admin_order_service import get_order_list_service, approve_order_service


def get_order_list_controller():
    """
    :description: interface with admin_dao, get all order list from CUI
    :return:
    """

    # Fetch the order list from the service layer
    order_list = get_order_list_service()
    if not order_list:
        print(Message.NO_PENDING_ORDERS.value)
        return

    # Initialize PrettyTable with column names
    table = PrettyTable()
    table.field_names = [
        "Order ID",
        "Customer ID",
        "Car ID",
        "Rental Start Date",
        "Rental End Date",
        "Total Cost",
        "Order Status",
        "Created at",
    ]

    # Add rows to the table
    for order in order_list:
        table.add_row([
            order.order_id,
            order.customer_id,
            order.car_id,
            order.rent_start_date,
            order.rent_end_date,
            order.total_cost,
            order.order_status,  # capsuled
            order.created_at,
        ])

    # Print the formatted table
    print(table)


def order_approve_controller():
    """
    :description: interface with admin_dao, approve or reject orders from CUI
    :return:
    """
    # Fetch the order list
    order_list = get_order_list_service()
    # select an order by id
    while True:
        try:
            input_order_id = input("Enter the id of the order you want to approve/reject: ")
            order_id_list = [order.order_id for order in order_list]
            if input_order_id not in order_id_list:
                print(Message.ORDER_NOT_FOUND.value)
                break
            else:
                # Ask for approval or rejection
                action = input("Enter 'approve' to approve the order or 'reject' to reject it: ").strip().lower()
                if action == "approve":
                    result = approve_order_service(input_order_id, True)
                    if result:
                        print(Message.ORDER_APPROVE_SUCCESSFUL.value)
                    else:
                        print(Message.ORDER_APPROVE_FAILED.value)
                elif action == "reject":
                    result = approve_order_service(input_order_id, False)
                    if result:
                        print(Message.ORDER_REJECT_SUCCESSFUL.value)
                    else:
                        print(Message.ORDER_REJECT_FAILED.value)
                else:
                    print(Message.INVALID_ACTION.value)
                break
        except Exception as e:
            print(f'Error: {e}')


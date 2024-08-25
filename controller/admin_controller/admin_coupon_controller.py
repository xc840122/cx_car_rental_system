"""
    @author: Peter
    @date: 23/08/2024
    @file: admin_coupon_controller.py
    @description: coupon related controller, interact with customer via CUI
"""
from datetime import datetime, date

from prettytable import PrettyTable

from dto.coupon_dto import CouponDto
from enum_entity.coupon_status import CouponStatus
from enum_entity.message import Message
from service.admin.admin_coupon_service import add_coupons_service, get_coupons_service


def add_coupons_controller():
    """
    :description: add coupons related controller
    :return:
    """
    try:
        # Prompt for the denomination and validate input
        denomination_input = input("Please input coupon denomination(NZD): ")
        denomination = float(denomination_input)
        if denomination <= 0:
            print("Denomination must be a positive value.")
            return

        description = input("Please input coupon description: ").strip()
        if not description:
            print("Description cannot be empty.")
            return

        # Validate status input
        status = input("Please input coupon status (PENDING or ACTIVATED): ").strip().upper()
        if status not in [CouponStatus.PENDING.value, CouponStatus.ACTIVATED.value]:
            print("Invalid coupon status. Allowed values are: PENDING, ACTIVATED.")
            return

        # Handle date input and validate format
        input_start_date = input("Please input coupon start date (DD-MM-YYYY): ")
        start_date = datetime.strptime(input_start_date, '%d-%m-%Y').date()

        input_expired_date = input("Please input coupon expired date (DD-MM-YYYY): ")
        expired_date = datetime.strptime(input_expired_date, '%d-%m-%Y').date()

        # Check if the start date is before the expired date
        if start_date >= expired_date:
            print("Start date must be before the expired date.")
            return

        # Input the number of coupons and validate
        coupon_numbers = int(input("Please input the number of coupons: "))
        if coupon_numbers <= 0:
            print("Number of coupons must be a positive integer.")
            return

        # Create the coupon DTO and call the service layer to add coupons
        coupon_dto = CouponDto(denomination, description, status, start_date, expired_date)
        result = add_coupons_service(coupon_dto, coupon_numbers)

        # Feedback to the user based on the service result
        if result:
            print(Message.COUPON_ADD_SUCCESSFUL.value)
        else:
            print(Message.COUPON_ADD_FAILED.value)
    except ValueError as ve:
        print(f"Invalid input: {ve}. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_coupons_controller():
    """
    :description: get coupons related controller by coupon status
    :return:
    """
    while True:
        # Prompt user for the coupon status and validate the input
        coupon_status = input("Please input coupon status (PENDING/ACTIVATED/USED/EXPIRED): ").strip().upper()

        if coupon_status not in [coupon_status.value for coupon_status in CouponStatus]:
            print(Message.INVALID_INPUT.value)
            continue

        # Fetch the coupon list from the service layer
        coupon_list = get_coupons_service(coupon_status)

        # Check if the coupon list is empty
        if not coupon_list:
            print(Message.NO_COUPONS_FOUND.value)
        else:
            # Initialize PrettyTable with column names
            table = PrettyTable()
            table.field_names = [
                "Coupon ID",
                "Denomination",
                "Description",
                "Status",
                "Start date",
                "Expired date",
                "Created at",
            ]

            # Add rows to the table
            for coupon in coupon_list:
                table.add_row([
                    coupon.coupon_id,
                    coupon.denomination,
                    coupon.description,
                    coupon.status,
                    coupon.start_date,
                    coupon.expired_date,
                    coupon.created_at,
                ])

            # Print the formatted table
            print(table)

        # Exit after fetching the list to prevent infinite loops
        break


def set_coupon_status_controller():
    """
    :description: not ready yet, for further expansion
    :return:
    """
    pass


def remove_coupon_controller():
    """
    :description: not ready yet, for further expansion
    :return:
    """
    pass

"""
    @author: Peter
    @date: 20/08/2024
    @file: customer_order_controller.py
    @description: order related controller of customer
"""

from prettytable import PrettyTable

from controller.customer_controller.customer_login_controller import current_login_customer
from dto.order_dto import OrderDto
from enum_entity.coupon_status import CouponStatus
from enum_entity.message import Message
from datetime import datetime
from service.customer.customer_car_service import customer_get_car_by_id_service
from service.customer.customer_coupon_service import verify_coupon_service, update_coupon_status_service
from service.customer.customer_order_service import customer_car_date_available_service, check_car_rental_days, \
    customer_order_car_service, get_customer_orders_service, calculate_final_cost_service


def customer_order_car_controller():
    """
    :description: Interface for customers to book a car
    :return: None
    """
    # input car_id ,validate is car exist
    ordered_car = get_valid_car_id()
    if ordered_car:
        car_id = ordered_car.car_id
    else:
        return False
    # input start date, validate
    start_date = get_valid_rental_start_date()
    # input end date, validate
    end_date = get_valid_rental_end_date(start_date)

    # validate car availability
    if not validate_car_availability(ordered_car, start_date, end_date):
        return
    # validate the duration
    if not validate_rental_duration(ordered_car, start_date, end_date):
        return
    # if use coupon, return validated coupon
    coupon_denomination = 0.0
    coupon = handle_coupon_application()
    if coupon:
        coupon_denomination = coupon.denomination

    # get customer_id from cached data
    customer_id = current_login_customer()
    # generate order_dto
    order_dto = OrderDto(customer_id, car_id, coupon.coupon_id if coupon else None, start_date, end_date)
    # calculate cost
    total_cost = calculate_total_cost(order_dto, coupon_denomination)
    # finalize order
    if confirm_order(total_cost):
        finalize_order(order_dto)


def get_customer_orders_controller():
    """
    :description: Interface for customers to view their order list
    """
    # get customer id from login cache
    customer_id = current_login_customer()
    # Fetch the order list
    order_list = get_customer_orders_service(customer_id)

    if not order_list:
        print("No orders found.")
        return

    # Initialize PrettyTable with column names
    table = PrettyTable()
    table.field_names = [
        "Order ID",
        "Car ID",
        "Start Date",
        "End Date",
        "Total Cost",
        "Status",
        "Created At"]

    # Add rows to the table
    for order in order_list:
        table.add_row([
            order.order_id,
            order.car_id,
            order.rent_start_date,
            order.rent_end_date,
            order.total_cost,
            order.order_status,
            order.created_at
        ])

    # Print the formatted table
    print(table)


def get_valid_car_id():
    """Prompt the user for a valid car ID and return the car ID and car details."""
    while True:
        try:
            car_id = int(input("Enter the car ID you wish to order: "))
            ordered_car = customer_get_car_by_id_service(car_id)
            if ordered_car is None:
                print(Message.CAR_NOT_FOUND.value)
                return
            else:
                return ordered_car
        except ValueError:
            print(Message.INVALID_INPUT.value)
            return


def get_valid_rental_start_date():
    """Prompt the user for a valid rental start date."""
    while True:
        rental_start_date = input("Enter the rental start date (DD-MM-YYYY): ")
        try:
            start_date = datetime.strptime(rental_start_date, "%d-%m-%Y").date()
            if start_date < datetime.now().date():
                print(Message.RENTAL_START_DATE_EARLIER_THAN_PRESENT_DATE.value)
            else:
                return start_date
        except ValueError:
            print(Message.INVALID_DATE_FORMAT.value)


def get_valid_rental_end_date(start_date):
    """Prompt the user for a valid rental end date."""
    while True:
        rental_end_date = input("Enter the rental end date (DD-MM-YYYY): ")
        try:
            end_date = datetime.strptime(rental_end_date, "%d-%m-%Y").date()
            if end_date < start_date:
                print(f'{Message.RENTAL_END_DATE_EARLIER_THAN_START_DATE.value}: {start_date} - {end_date}')
            else:
                return end_date
        except ValueError:
            print(Message.INVALID_DATE_FORMAT.value)


def validate_car_availability(ordered_car, start_date, end_date):
    """Check if the car is available for the selected period."""
    if not customer_car_date_available_service(ordered_car, start_date, end_date):
        print(Message.RENTAL_DAYS_NOT_AVAILABLE.value)
        return False
    return True


def validate_rental_duration(ordered_car, start_date, end_date):
    """Check if the rental duration is within allowed limits."""
    if not check_car_rental_days(ordered_car, start_date, end_date):
        print(f"Rental period must be between {ordered_car.min_rent_period} and {ordered_car.max_rent_period} days.")
        return False
    return True


def handle_coupon_application():
    """Handle the coupon application process and return the coupon and its denomination."""
    # check use coupon
    use_coupon = input("Do you want to use a coupon(no cash return "
                       "if denomination is more than order amount? (yes/no): ").strip().lower()
    if use_coupon == 'yes':
        coupon_id = input("Please enter your coupon id: ").strip()
        # verify coupon
        coupon = verify_coupon_service(coupon_id)
    else:
        return False

    # validate coupon if use
    if coupon:
        if (coupon.status == CouponStatus.ACTIVATED.value and
                coupon.start_date <= datetime.now().date() <= coupon.expired_date):
            coupon_denomination = coupon.denomination
            print(f"{Message.COUPON_APPLIED.value}, you can save {coupon_denomination} NZD.")
        else:
            print(Message.INVALID_COUPON_STATUS.value if coupon else Message.INVALID_COUPON_ID.value)
            coupon = None
    return coupon


def calculate_total_cost(order_dto, coupon_denomination):
    """Calculate the total cost of the order after applying the coupon discount."""
    total_cost = calculate_final_cost_service(order_dto)
    if coupon_denomination > 0:
        print(f"{Message.APPLY_COUPON_SUCCESSFUL.value} {total_cost} NZD")
    else:
        print(f"{Message.APPLY_COUPON_FAILED.value}{total_cost} NZD.")
    return total_cost


def confirm_order(total_cost):
    """Ask the customer to confirm the order and return their choice."""
    confirm_the_order = input("Do you want to confirm the order? (yes/no): ").strip().lower()
    if confirm_the_order == 'yes':
        return True
    else:
        print(Message.ORDER_CANCELLED.value)
        return False


def finalize_order(order_dto):
    """Complete the order process and update the coupon status if necessary."""
    if customer_order_car_service(order_dto):
        print(Message.CAR_ORDER_SUCCESSFUL.value)
    else:
        print(Message.FAILED_TO_PLACE_ORDER.value)

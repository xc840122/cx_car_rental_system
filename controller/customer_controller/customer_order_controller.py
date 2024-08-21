"""
    @author: Peter
    @date: 20/08/2024
    @file: customer_order_controller.py
    @description: order related controller of customer
"""
from prettytable import PrettyTable

from controller.customer_controller.customer_login_controller import current_login_customer
from dto.order_dto import OrderDto
from enum_entity.message import Message
from datetime import datetime
from service.customer.customer_car_service import customer_get_car_by_id_service
from service.customer.customer_order_service import customer_car_date_available_service, check_car_rental_days, \
    customer_order_car_service, get_customer_orders_service


def customer_order_car_controller():
    """
        :description: Interface for customers to book a car
        :return:
    """
    # Step 1: Get and validate car_id
    while True:
        try:
            car_id = int(input("Enter the car ID you wish to order: "))
            ordered_car = customer_get_car_by_id_service(car_id)
            # Verify if car_id exists and the car is available
            if ordered_car is None:
                print(Message.CAR_NOT_FOUND.value)
            else:
                break
        except Exception as e:
            print(f'{Message.INVALID_INPUT.value}')

    # Step 2: Get and validate rental_start_date
    while True:
        rental_start_date = input("Enter the rental start date (DD-MM-YYYY): ")
        try:
            start_date = datetime.strptime(rental_start_date, "%d-%m-%Y").date()
            if start_date < datetime.now().date():
                print(Message.RENTAL_START_DATE_EARLIER_THAN_PRESENT_DATE.value)
            else:
                break
        except Exception as e:
            print(f'{Message.INVALID_DATE_FORMAT.value}')

    # Step 3: Get and validate rental_end_date
    while True:
        rental_end_date = input("Enter the rental end date (DD-MM-YYYY): ")
        try:
            end_date = datetime.strptime(rental_end_date, "%d-%m-%Y").date()
            if end_date < start_date:
                print(f'{Message.RENTAL_END_DATE_EARLIER_THAN_START_DATE.value}: {start_date} - {end_date}')
            else:
                break
        except Exception as e:
            print(f'{Message.INVALID_DATE_FORMAT.value}: {e}')

    # Step 4: Additional logic to check car availability during the selected period
    if not customer_car_date_available_service(ordered_car, start_date, end_date):
        print(Message.RENTAL_DAYS_NOT_AVAILABLE.value)
        return

    # Step 5: check the renting duration with minimal/maximum rent days of the car
    if not check_car_rental_days(ordered_car, start_date, end_date):
        print(f"Rental period must be between {ordered_car.min_rent_period} and {ordered_car.max_rent_period} days.")
        return

    # step 6: get customer_id from login cache, generate OrderDto object
    customer_id = current_login_customer()
    order_dto = OrderDto(customer_id, car_id, start_date, end_date)

    # Step 7: Proceed with the order process
    customer_order_car_service(order_dto)
    print(Message.CAR_ORDER_SUCCESSFUL.value)


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
            order.status,
            order.created_at
        ])

    # Print the formatted table
    print(table)


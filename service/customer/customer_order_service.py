"""
    @author: Peter
    @date: 21/08/2024
    @file: customer_order_service.py
    @description: order logic of customer
"""
from datetime import date, datetime

from dao.customer_dao.customer_car_dao import customer_get_car_by_id
from dao.customer_dao.customer_order_dao import customer_car_date_available, customer_order_car, get_customer_orders
from dto.order_dto import OrderDto
from entity.car import Car
from entity.order import Order
from utils.generate_id import generate_order_id


def customer_car_date_available_service(car: Car, start_date: date, end_date: date) -> bool:
    """
    :param car:
    :description: Check if the car is available for the given date range
    :param car_id: ID of the car to check
    :param start_date: Rental start date (YYYY-MM-DD)
    :param end_date: Rental end date (YYYY-MM-DD)
    :return: True if the car is available, False otherwise
    """
    return customer_car_date_available(car.car_id, start_date, end_date)


def check_car_rental_days(car: Car, rent_start_date: date, rent_end_date: date) -> bool:
    """
    :description: Check if the rental period for a car is within the allowed min and max rental days.
    :param car_id: car_id for selecting a car, then get max and min rental days
    :param rent_start_date: Rental start date as a string in 'YYYY-MM-DD' format.
    :param rent_end_date: Rental end date as a string in 'YYYY-MM-DD' format.
    :return: True if the rental period is valid, False otherwise.
    """
    try:
        # Calculate the total rental period in days
        rental_days = (rent_end_date - rent_start_date).days + 1
        # get car object, and min, max rental days
        car = customer_get_car_by_id(car.car_id)
        # Check if the rental period is within the allowed min and max rental days
        if car.min_rent_period <= rental_days <= car.max_rent_period:
            return True
        else:
            return False

    except ValueError as e:
        print(f"Date format error: {e}")
        return False


def customer_order_car_service(order_dto: OrderDto) -> bool:
    """
    :description: Service to order a car for a customer
    :param order_dto: Data Transfer Object with ordering information
    :return: Boolean indicating success of the booking operation
    """
    # order id
    order_id = generate_order_id()
    # customer id
    customer_id = order_dto.user_id
    # car id
    car_id = order_dto.car_id
    # rent start date
    rent_start_date = order_dto.rental_start_date
    # rent end date
    rent_end_date = order_dto.rental_end_date

    # get car object according to car_id
    ordered_car = customer_get_car_by_id(car_id)

    # calculate total_cost according to unit_price and rental duration
    total_rent_days = (rent_end_date - rent_start_date).days + 1
    total_cost = ordered_car.unit_price * total_rent_days

    # generate Order object
    order = Order(order_id, customer_id, car_id, rent_start_date,
                  rent_end_date, total_cost)
    return customer_order_car(order)


def get_customer_orders_service(customer_id: str) -> list[Order]:
    """
    :param customer_id: ID of the customer
    :return: List of Order objects
    :description: Service layer to get all orders of a customer
    """
    return get_customer_orders(customer_id)


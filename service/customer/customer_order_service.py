"""
    @author: Peter
    @date: 21/08/2024
    @file: customer_order_service.py
    @description: order logic of customer
"""
from datetime import date

from dao.customer_dao.customer_car_dao import customer_get_car_by_id
from dao.customer_dao.customer_order_dao import customer_car_date_available, customer_order_car, get_customer_orders
from dto.order_dto import OrderDto
from entity.car import Car
from entity.order import Order
from enum_entity.coupon_status import CouponStatus
from service.customer.customer_car_service import customer_get_car_by_id_service
from service.customer.customer_coupon_service import verify_coupon_service, update_coupon_status_service
from utils.generate_id import generate_order_id


def customer_car_date_available_service(car: Car, start_date: date, end_date: date) -> bool:
    """
    :param car:
    :description: Check if the car is available for the given date range
    :param car: object of the car to check
    :param start_date: Rental start date (YYYY-MM-DD)
    :param end_date: Rental end date (YYYY-MM-DD)
    :return: True if the car is available, False otherwise
    """
    count = customer_car_date_available(car.car_id, start_date, end_date)
    # no conflict
    if count == 0:
        return True
    # conflict with other orders
    else:
        return False


def check_car_rental_days(car: Car, rent_start_date: date, rent_end_date: date) -> bool:
    """
    :description: Check if the rental period for a car is within the allowed min and max rental days.
    :param car: car for selecting a car, then get max and min rental days
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
    # coupon id
    coupon_id = order_dto.coupon_id
    # rent start date
    rent_start_date = order_dto.rental_start_date
    # rent end date
    rent_end_date = order_dto.rental_end_date

    # calculate total_cost according to unit_price and rental duration
    total_cost = calculate_final_cost_service(order_dto)

    # generate Order object
    order = Order(order_id, customer_id, car_id, coupon_id, rent_start_date,
                  rent_end_date, total_cost)

    # result
    result = customer_order_car(order)
    if result:
        if order_dto.coupon_id:
            update_coupon_status_service(order_dto.coupon_id, CouponStatus.USED.value)
            return True
        return True
    else:
        return False


def get_customer_orders_service(customer_id: str) -> list[Order]:
    """
    :param customer_id: ID of the customer
    :return: List of Order objects
    :description: Service layer to get all orders of a customer
    """
    return get_customer_orders(customer_id)


def calculate_final_cost_service(order_dto: OrderDto) -> float:
    """
    :description: Service to calculate the final cost of a customer
    :param order_dto: Data Transfer Object with ordering information
    :return:
    """
    # get rental days
    total_rental_days = (
            (order_dto.rental_end_date - order_dto.rental_start_date).days + 1)
    # get car object
    car = customer_get_car_by_id_service(order_dto.car_id)
    # get unit_price
    car_unit_price = car.unit_price
    # calculate base cost
    base_cost = car_unit_price * total_rental_days
    # verify and get coupon object
    coupon = verify_coupon_service(order_dto.coupon_id)
    if coupon:
        # calculate total cost with coupon denomination
        total_cost = base_cost - coupon.denomination
        # Ensure that total cost is not negative
        total_cost = max(float(0), total_cost)
        return total_cost
    else:
        return base_cost

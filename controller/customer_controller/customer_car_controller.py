"""
    @author: Peter
    @date: 21/08/2024
    @file: customer_car_controller.py
    @description: car related controller for customer
"""
from prettytable import PrettyTable
from constant.car_columns import CAR_COLUMNS
from service.customer.customer_car_service import customer_get_car_list_service


def customer_get_car_list_controller():
    """
    :description: get all cars list from CUI
    :return:
    """
    # Initialize PrettyTable with column names
    table = PrettyTable()
    table.field_names = [
        CAR_COLUMNS["CAR_ID"],
        CAR_COLUMNS["MAKE"],
        CAR_COLUMNS["MODEL"],
        CAR_COLUMNS["YEAR"],
        CAR_COLUMNS["MILEAGE"],
        CAR_COLUMNS["UNIT_PRICE"],
        CAR_COLUMNS["MIN_RENT_PERIOD"],
        CAR_COLUMNS["MAX_RENT_PERIOD"]
    ]

    # Fetch the car list,present cars that available !=0
    car_list = customer_get_car_list_service()
    # Add rows to the table
    for car in car_list:
        table.add_row([
            car.car_id,
            car.make,
            car.model,
            car.year,
            car.mileage,
            car.unit_price,
            car.min_rent_period,
            car.max_rent_period
        ])

    # Print the formatted table
    print(table)

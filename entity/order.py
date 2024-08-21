"""
    @author: Peter
    @date: 21/08/2024
    @file: order.py
    @description: order entity
"""
from datetime import datetime, date
from decimal import Decimal


class Order:
    def __init__(self, order_id: str, customer_id: str, car_id: int, rent_start_date: date, rent_end_date: date,
                 total_cost: Decimal, status: str = 'PENDING', created_at: str = None):
        """
        :description: Initialize an Order object.
        :param order_id: Unique ID of the order.
        :param customer_id: ID of the customer placing the order.
        :param car_id: ID of the car being rented.
        :param rent_start_date: Start date of the rental period (YYYY-MM-DD).
        :param rent_end_date: End date of the rental period (YYYY-MM-DD).
        :param total_cost: Total cost of the rental.
        :param status: Status of the order (default is 'PENDING').
        :param created_at: Timestamp of when the order was created.
        """
        self.order_id = order_id
        self.customer_id = customer_id
        self.car_id = car_id
        self.rent_start_date = rent_start_date
        self.rent_end_date = rent_end_date
        self.total_cost = Decimal(total_cost)
        self.status = status # pending,rejected,approved,complete
        self.created_at = created_at or datetime.now()

    def __str__(self):
        return (f"Order ID: {self.order_id}, Customer ID: {self.customer_id}, Car ID: {self.car_id}, "
                f"Rental Period: {self.rent_start_date.date()} to {self.rent_end_date.date()}, "
                f"Total Cost: {self.total_cost}, Status: {self.status}, Created At: {self.created_at}")

    def update_status(self, new_status: str):
        """
        :description: Update the status of the order.
        :param new_status: New status for the order.
        """
        valid_statuses = ['PENDING', 'APPROVED', 'REJECTED', 'COMPLETED']
        if new_status.upper() in valid_statuses:
            self.status = new_status.upper()
        else:
            print("Invalid status provided.")

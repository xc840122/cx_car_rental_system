"""
    @author: Peter
    @date: 21/08/2024
    @file: order_dto.py
    @description: order information transmission
"""


class OrderDto:
    def __init__(self, user_id, car_id, rental_start_date, rental_end_date):
        self.user_id = user_id
        self.car_id = car_id
        self.rental_start_date = rental_start_date
        self.rental_end_date = rental_end_date

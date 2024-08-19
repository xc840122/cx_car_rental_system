"""
    @author: Peter
    @date: 19/08/2024
    @file: car.py
    @description: car object
"""


class Car:
    def __init__(self, car_id, make, model, year, mileage, unit_price, min_rent_period, max_rent_period, available=0):
        self.car_id: int = car_id
        self.make: str = make
        self.model: str = model
        self.year: int = year
        self.mileage: int = mileage
        self.available: int = available
        self.unit_price: float = unit_price
        self.min_rent_period: int = min_rent_period
        self.max_rent_period: int = max_rent_period

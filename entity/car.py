"""
    @author: Peter
    @date: 19/08/2024
    @file: car.py
    @description: car object
"""


class Car:
    def __init__(self, car_id, make, model, year, mileage, available, unit_price, min_rent_period, max_rent_period):
        self.car_id: int = car_id
        self.make: str = make
        self.model: str = model
        self.year: int = year
        self.mileage: int = mileage
        self.available: int = available  # 0,hide, 1,normal, 2, rented
        self.unit_price: float = unit_price
        self.min_rent_period: int = min_rent_period
        self.max_rent_period: int = max_rent_period

    def __str__(self):
        return (f'car_id={self.car_id}, make={self.make},model= {self.model}, year={self.year}, '
                f'mileage={self.mileage}, available={self.available},unit_price={self.unit_price}, '
                f'min={self.min_rent_period}, '
                f'max={self.max_rent_period}, ')

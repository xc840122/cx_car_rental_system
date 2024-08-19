"""
    @author: Peter
    @date: 19/08/2024
    @file: car_dto.py
    @description: visual object of car information which are shown on CUI
"""


class CarDto:
    def __init__(self,make, model, year, mileage, unit_price, min_rent_period, max_rent_period):
        self.make: str = make
        self.model: str = model
        self.year: int = year
        self.mileage: int = mileage
        self.unit_price: float = unit_price
        self.min_rent_period: int = min_rent_period
        self.max_rent_period: int = max_rent_period

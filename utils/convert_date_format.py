"""
    @author: Peter
    @date: 25/08/2024
    @file: convert_data_format.py
    @description: convert str from db, YYYY-mm-dd to date obj dd-mm-YYYY
"""
from datetime import datetime


def convert_date_format(date_str):
    """
    Converts a date string from YYYY-mm-dd to dd-mm-YYYY format.

    :param date_str: A string representing a date in YYYY-mm-dd format.
    :return: A string representing the date in dd-mm-YYYY format.
    """
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        new_date_str = date_obj.strftime("%d-%m-%Y")
        new_date_obj = datetime.strptime(new_date_str, "%d-%m-%Y").date()
        return new_date_obj
    except ValueError as e:
        print(f"Error converting date format: {e}")
        return None

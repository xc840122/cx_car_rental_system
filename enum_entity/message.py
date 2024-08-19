"""
    @author: Peter
    @date: 18/08/2024
    @file: message.py
    @description: various messages of reminder, feedback,warning to end user
"""
from enum import Enum


class Message(Enum):
    USERNAME_ALREADY_EXISTS = "user_name already exists"
    LICENSE_NO_ALREADY_EXISTS = "license no already exists"
    PHONE_ALREADY_EXISTS = "phone already exists"
    CUSTOMER_LOGIN_SUCCESSFUL = "Welcome, dear customer, Login Successful"
    CUSTOMER_LOGIN_FAILED = "Sorry, dear customer, Login Failed"
    ADMIN_LOGIN_SUCCESSFUL = "Go to work!!!, Login Successful"
    ADMIN_LOGIN_FAILED = "Don't want to work? Login Failed"
    ADD_CAR_SUCCESSFUL = "The car has been added"
    ADD_CAR_FAILED = "The car has not been added"
    INVALID_ID = "Invalid id. Please try again."
    CAR_NOT_FOUND = "car doesn't exist. Please try again."
    INPUT_VALID_INTEGER = "Please enter a valid integer."

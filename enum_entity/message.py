"""
    @author: Peter
    @date: 18/08/2024
    @file: message.py
    @description: various messages of reminder, feedback,warning to end user
"""
from enum import Enum


class Message(Enum):
    NO_CHANGE_WITH_NULL = "\n### Update values as long as new value input ###\n"
    REGISTRATION_FAILED = "Sign up failed"
    REGISTRATION_SUCCESSFUL = "Sign up successful"
    PASSWORD_MISMATCH = "The two password are not same, sign up failed"
    ADMIN_LOGIN_SUCCESSFUL = "Go to work!!!, Login Successful"
    ADMIN_LOGIN_FAILED = "Don't want to work? Login Failed"
    ADD_CAR_SUCCESSFUL = "The car has been added"
    ADD_CAR_FAILED = "The car has not been added"
    CUSTOMER_LOGIN_SUCCESSFUL = "Welcome, dear customer, Login Successful"
    CUSTOMER_LOGIN_FAILED = "Sorry, dear customer, Login Failed"
    CAR_NOT_FOUND = "car doesn't exist. Please try again."
    CAR_ORDER_SUCCESSFUL = "Car ordering successful, please wait for auditing!"
    DELETE_CAR_SUCCESSFUL = "The car has been deleted"
    DELETE_CAR_FAILED = "The car has been deleted"
    EXIT_SYSTEM = "Exiting the system. Goodbye!"
    INVALID_INPUT = "invalid input"
    INVALID_ACTION = "invalid action"
    INVALID_ID = "Invalid id. Please try again."
    INVALID_ORDER_ID = "Invalid order id. Please try again."
    INVALID_DATE_FORMAT = "Invalid date format, Please enter the date in YYYY-MM-DD format."
    INVALID_CHOICE = "Invalid choice. Please try again."
    INPUT_VALID_INTEGER = "Please enter a valid integer."
    LICENSE_NO_ALREADY_EXISTS = "license no already exists"
    LOG_OUT = "Logging out...Goodbye"
    LEAVE = "Leaving...Goodbye"
    NOT_EMPTY_USERNAME_OR_PASSWORD = "Username or password cannot be empty."
    NO_PENDING_ORDERS = "No pending orders"
    ORDER_REJECT_FAILED = "order reject failed"
    ORDER_REJECT_SUCCESSFUL = "order reject successful"
    ORDER_APPROVE_FAILED = "order approved failed"
    ORDER_APPROVE_SUCCESSFUL = "order approved successful"
    ORDER_NOT_FOUND = "order not found"
    PHONE_ALREADY_EXISTS = "phone already exists"
    RENTAL_END_DATE_EARLIER_THAN_START_DATE = "Rental end date cannot be earlier than the start date."
    RENTAL_START_DATE_EARLIER_THAN_PRESENT_DATE = "Rental start date cannot be earlier than the present date."
    RENTAL_DAYS_NOT_AVAILABLE = "The selected car is already rented for the specified dates"
    USERNAME_AND_PASSWORD_LENGTH = "Username must be at least 3 characters and password at least 6 characters long."
    USERNAME_AND_PASSWORD_FORMAT = "Username cannot contain '@' or spaces"
    USERNAME_ALREADY_EXISTS = "user_name already exists"

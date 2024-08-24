"""
    @author: Peter
    @date: 16/08/2024
    @file: initial_db.py
    @description: database schema, create table to initial database
"""
from constant.db_config import CREATE_DATABASE_CONFIG, SETUP_DATABASE_CONFIG
from utils.connect_db import get_connection, create_database_connection
from utils.release_db import commit_and_close_connection


def setup_database():
    # create database
    create_conn = create_database_connection()
    create_cursor = create_conn.cursor()

    create_cursor.execute('''CREATE DATABASE IF NOT EXISTS cx_cars''')
    commit_and_close_connection(create_conn)

    # connect database, initial database
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS admins (
                        user_id VARCHAR(50) PRIMARY KEY,
                        user_name VARCHAR(20) NOT NULL UNIQUE ,
                        password VARCHAR(20) NOT NULL,
                        branch_code INT(5) NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                            user_id VARCHAR(50) PRIMARY KEY,
                            user_name VARCHAR(20) NOT NULL UNIQUE ,
                            password VARCHAR(20) NOT NULL,
                            name VARCHAR(100) NOT NULL,
                            license_no VARCHAR(100) NOT NULL UNIQUE,
                            phone VARCHAR(20) NOT NULL UNIQUE,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                        )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
                            car_id INT AUTO_INCREMENT PRIMARY KEY,
                            make VARCHAR(50) NOT NULL,
                            model VARCHAR(50) NOT NULL,
                            year INT NOT NULL,
                            mileage INT NOT NULL,
                            available TINYINT NOT NULL DEFAULT 1, # 0:not available, 1: normal, 2: rented
                            unit_price FLOAT NOT NULL,
                            min_rent_period INT NOT NULL,
                            max_rent_period INT NOT NULL,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                        )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS car_rental_orders (
                            order_id VARCHAR(50) PRIMARY KEY,
                            customer_id VARCHAR(50) NOT NULL,
                            car_id INT NOT NULL,
                            coupon_id VARCHAR(50),
                            rent_start_date DATE NOT NULL,
                            rent_end_date DATE NOT NULL,
                            total_cost DECIMAL(10, 2) NOT NULL,
                            status ENUM('PENDING', 'APPROVED', 'REJECTED', 'COMPLETED') DEFAULT 'PENDING',
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                            INDEX idx_customer_id (customer_id),
                            INDEX idx_car_id (car_id),
                            INDEX idx_coupon_id (coupon_id),
                            INDEX idx_rent_dates (rent_start_date, rent_end_date)
                        )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS coupons (
                            coupon_id VARCHAR(50) PRIMARY KEY,
                            denomination DECIMAL(10, 2) NOT NULL,
                            description VARCHAR(100) NOT NULL,
                            status ENUM('PENDING', 'ACTIVATED', 'USED', 'EXPIRED') DEFAULT 'PENDING',
                            start_date DATE NOT NULL,
                            expired_date DATE NOT NULL,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                        )''')

    commit_and_close_connection(conn)

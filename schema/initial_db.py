"""
    @author: Peter
    @date: 16/08/2024
    @file: initial_db.py
    @description: database schema, create table to initial database
"""
# import mysql.connector
# from constant.db_config import DATABASE_CONFIG
from utils.connect_db import get_connection


def setup_database():
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
                            available TINYINT NOT NULL DEFAULT 1,
                            unit_price FLOAT NOT NULL,
                            min_rent_period INT NOT NULL,
                            max_rent_period INT NOT NULL,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                        )''')
    conn.commit()
    conn.close()

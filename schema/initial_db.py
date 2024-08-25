"""
    @author: Peter
    @date: 16/08/2024
    @file: initial_db.py
    @description: database schema, create table to initial database
"""
from utils.connect_db import get_connection


def setup_database():
    # connect to the database and initialize the schema
    conn = get_connection()
    cursor = conn.cursor()

    # Create the admins table
    cursor.execute('''CREATE TABLE IF NOT EXISTS admins (
                        user_id VARCHAR(50) PRIMARY KEY,
                        user_name VARCHAR(20) NOT NULL UNIQUE,
                        password VARCHAR(20) NOT NULL,
                        branch_code INTEGER NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')

    # Create the customers table
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                        user_id VARCHAR(50) PRIMARY KEY,
                        user_name VARCHAR(20) NOT NULL UNIQUE,
                        password VARCHAR(20) NOT NULL,
                        name VARCHAR(100) NOT NULL,
                        license_no VARCHAR(100) NOT NULL UNIQUE,
                        phone VARCHAR(20) NOT NULL UNIQUE,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')

    # Create the cars table
    cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
                        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        make VARCHAR(50) NOT NULL,
                        model VARCHAR(50) NOT NULL,
                        year INTEGER NOT NULL,
                        mileage INTEGER NOT NULL,
                        available INTEGER NOT NULL DEFAULT 1, -- 0:not available, 1: normal, 2: rented
                        unit_price FLOAT NOT NULL,
                        min_rent_period INTEGER NOT NULL,
                        max_rent_period INTEGER NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')

    # Create the car_rental_orders table
    cursor.execute('''CREATE TABLE IF NOT EXISTS car_rental_orders (
                        order_id VARCHAR(50) PRIMARY KEY,
                        customer_id VARCHAR(50) NOT NULL,
                        car_id INTEGER NOT NULL,
                        coupon_id VARCHAR(50),
                        rent_start_date DATE NOT NULL,
                        rent_end_date DATE NOT NULL,
                        total_cost FLOAT(10,2) NOT NULL,
                        status VARCHAR(50) DEFAULT 'PENDING',
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')

    # Create the coupons table
    cursor.execute('''CREATE TABLE IF NOT EXISTS coupons (
                        coupon_id VARCHAR(50) PRIMARY KEY,
                        denomination FLOAT(10, 2) NOT NULL,
                        description VARCHAR(100) NOT NULL,
                        status TEXT CHECK(status IN ('PENDING', 'ACTIVATED', 'USED', 'EXPIRED')) DEFAULT 'PENDING',
                        start_date DATE NOT NULL,
                        expired_date DATE NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')

    # Create indexes for car_rental_orders
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_customer_id ON car_rental_orders (customer_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_car_id ON car_rental_orders (car_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_coupon_id ON car_rental_orders (coupon_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_rent_dates ON car_rental_orders (rent_start_date, rent_end_date)')

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()


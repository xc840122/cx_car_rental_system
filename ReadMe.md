# **CX Car Rental System**
The **CX Car Rental System** is a Python-based CUI (command user interface) application designed to simplify car rental operations for both customers and administrators. This system allows customers to easily book cars, apply discount coupons, and manage their rental orders. For administrators, it offers functionalities for managing car inventories, coupons and orders.
## **Features**

- **Registration and Login**: Secure login and registration for customers and admins.
- **Car Management**: Administrators can add, update, or remove cars from the system.
- **Real-time Car Availability**: Ensures customers can only book cars that are available for the desired period.
- **Order Management**: Customers can create, view, and manage their car rental orders.
- **Order Audit: **Admin can audit the orders, approve or reject.
- **Order Conflict detect: **System detects order date and status for customer rental.
- **Coupon Management**: The system supports the creation and application of discount coupons
- **Automated Return Coupon**: Reset coupon status once related order is rejected
# Getting Started
## Running Project
To start the Car Rental System, follow these steps:

1. **Copy the code:**
   1. **Copy from zip file**: **You can decompress "CX Car Rental_source code.zip", copy all files into your local python project, or you can clone if from github which is described below.
   2. **Clone the Repository**: clone the repository to your local machine using the following command:
```
git clone https://github.com/xc840122/cx_car_rental_system.git
cd car-rental-system
```

2. **Set Up the Virtual Environment**: It’s recommended to use a virtual environment to manage dependencies. You can create and activate a virtual environment with the following commands:
```
python -m venv .venv
# On Windows
.\.venv\Scripts\activate
# On macOS and Linux
source .venv/bin/activate
```

3. **Install Dependencies**: Install the required Python packages by running:
```
pip install -r requirements.txt
```

4. **Run the Application**: Start the application by running the main script:
```
python main.py
```
This command will launch the Car Rental System, and you can interact with it through the command-line interface.

5. **Access the System**: Follow the prompts in the command line to navigate through the different menus and functionalities of the Car Rental System.
6. **Shut Down the Application**: To safely exit the system, follow the exit options provided in the menu or close the terminal window.
## Running the Builded Application
To start the Car Rental System:

1. unzip cx_car_rental_app for mac.zip/cx_car_rental_app for windows.zip file.
2. find file "main" in folder "main".
3. double click file "main" to start app.
4. Follow the On-Screen Instructions.

The application will guide you for both customers and administrators features.
### main menu
sign up as admin or customer, then login to get related sub-menu.
### admin menu
login in as admin, system presents admin menu.
### customer menu
login in as customer, system presents customer menu.
# Project Structure
## File Tree
The project is organized into several directories and files, each serving a specific purpose:
```
├── README.md
├── abstract_entity
│   ├── __init__.py
│   ├── menu.py
│   └── user.py
├── constant
│   ├── __init__.py
│   ├── car_columns.py
│   └── db_config.py
├── controller
│   ├── __init__.py
│   ├── admin_controller
│   │   ├── __init__.py
│   │   ├── admin_car_controller.py
│   │   ├── admin_coupon_controller.py
│   │   ├── admin_login_controller.py
│   │   ├── admin_order_controller.py
│   │   └── admin_registration_controller.py
│   └── customer_controller
│       ├── __init__.py
│       ├── customer_car_controller.py
│       ├── customer_login_controller.py
│       ├── customer_order_controller.py
│       └── customer_registration_controller.py
├── cx_car_rental.db
├── dao
│   ├── __init__.py
│   ├── admin_dao
│   │   ├── __init__.py
│   │   ├── admin_car_dao.py
│   │   ├── admin_coupon_dao.py
│   │   ├── admin_login_dao.py
│   │   ├── admin_order_dao.py
│   │   └── admin_registration_dao.py
│   └── customer_dao
│       ├── __init__.py
│       ├── customer_car_dao.py
│       ├── customer_coupon_dao.py
│       ├── customer_login_dao.py
│       ├── customer_order_dao.py
│       └── customer_registration_dao.py
├── dto
│   ├── __init__.py
│   ├── admin_dto.py
│   ├── car_dto.py
│   ├── coupon_dto.py
│   ├── customer_dto.py
│   ├── login_dto.py
│   └── order_dto.py
├── entity
│   ├── __init__.py
│   ├── admin.py
│   ├── car.py
│   ├── coupon.py
│   ├── customer.py
│   ├── login_cache.py
│   └── order.py
├── enum_entity
│   ├── __init__.py
│   ├── car_make.py
│   ├── car_model.py
│   ├── coupon_status.py
│   ├── message.py
│   └── order_status.py
├── exception
│   ├── __init__.py
│   └── duplicated_exception.py
├── identifier.sqlite
├── main.py
├── main.spec
├── menu
│   ├── __init__.py
│   ├── admin_menu.py
│   ├── customer_menu.py
│   ├── decorator
│   │   ├── __init__.py
│   │   ├── base_menu_decorator.py
│   │   └── head_foot_decorator.py
│   └── main_menu.py
├── requirements.txt
├── schema
│   ├── __init__.py
│   └── initial_db.py
├── service
│   ├── __init__.py
│   ├── admin
│   │   ├── __init__.py
│   │   ├── admin_car_service.py
│   │   ├── admin_coupon_service.py
│   │   ├── admin_login_service.py
│   │   ├── admin_order_service.py
│   │   └── admin_registration_service.py
│   └── customer
│       ├── __init__.py
│       ├── customer_car_service.py
│       ├── customer_coupon_service.py
│       ├── customer_login_service.py
│       ├── customer_order_service.py
│       └── customer_registration_service.py
└── utils
    ├── __init__.py
    ├── check_if_duplicated.py
    ├── connect_db.py
    ├── convert_date_format.py
    ├── fee_caculation.py
    ├── generate_id.py
    ├── input_format_verification.py
    └── release_db.py

```
## Purpose of Each File
### Root Directory

- **README.md**: Provides an overview of the project, including setup instructions, features, and usage guidelines.
### abstract_entity

- **init.py**: Initializes the `abstract_entity` module.
- **menu.py**: Defines abstract classes or interfaces related to menu operations in the car rental system.
- **user.py**: Defines abstract classes or interfaces related to user operations, including methods that need to be implemented by specific user types (e.g., admin, customer).
### constant

- **init.py**: Initializes the `constant` module.
- **car_columns.py**: Contains constants representing the column names for the car-related tables shown on menu.
- **db_config.py**: Contains mysql database configuration settings, since the project has switched to sqlite, this is reserved file now,
### controller

- **init.py**: Initializes the `controller` module.
- **admin_controller**: Contains controllers for admin-specific operations:
   - **init.py**: Initializes the `admin_controller` submodule.
   - **admin_car_controller.py**: Handles car management operations for admins.
   - **admin_coupon_controller.py**: Manages coupon operations for admins.
   - **admin_login_controller.py**: Handles admin login functionalities.
   - **admin_order_controller.py**: Manages order operations for admins.
   - **admin_registration_controller.py**: Handles the registration of new admin users.
- **customer_controller**: Contains controllers for customer-specific operations:
   - **init.py**: Initializes the `customer_controller` submodule.
   - **customer_car_controller.py**: Handles car selection and viewing operations for customers.
   - **customer_login_controller.py**: Manages customer login functionalities.
   - **customer_order_controller.py**: Handles order-related operations for customers.
   - **customer_registration_controller.py**: Manages the registration process for new customers.
### Database Files

- **cx_car_rental.db**: The main SQLite database file storing all data related to the car rental system.
- **identifier.sqlite**: Another SQLite database file, potentially used for managing unique identifiers or other specific information.
### dao (Data Access Object)

- **init.py**: Initializes the `dao` module.
- **admin_dao**: Contains data access objects for admin-related data operations:
   - **init.py**: Initializes the `admin_dao` submodule.
   - **admin_car_dao.py**: Handles database operations related to car management for admins.
   - **admin_coupon_dao.py**: Manages coupon-related data operations for admins.
   - **admin_login_dao.py**: Handles data operations for admin login functionality.
   - **admin_order_dao.py**: Manages order-related data operations for admins.
   - **admin_registration_dao.py**: Handles data operations related to admin registration.
- **customer_dao**: Contains data access objects for customer-related data operations:
   - **init.py**: Initializes the `customer_dao` submodule.
   - **customer_car_dao.py**: Handles car-related data operations for customers.
   - **customer_coupon_dao.py**: Manages coupon-related data operations for customers.
   - **customer_login_dao.py**: Handles data operations for customer login functionality.
   - **customer_order_dao.py**: Manages order-related data operations for customers.
   - **customer_registration_dao.py**: Handles data operations related to customer registration.
### dto (Data Transfer Object)

- **init.py**: Initializes the `dto` module.
- **admin_dto.py**: Defines data transfer objects for admin data.
- **car_dto.py**: Defines data transfer objects for car data.
- **coupon_dto.py**: Defines data transfer objects for coupon data.
- **customer_dto.py**: Defines data transfer objects for customer data.
- **login_dto.py**: Defines data transfer objects for login data.
- **order_dto.py**: Defines data transfer objects for order data.
### entity

- **init.py**: Initializes the `entity` module.
- **admin.py**: Defines the `Admin` entity class and its properties.
- **car.py**: Defines the `Car` entity class and its properties.
- **coupon.py**: Defines the `Coupon` entity class and its properties.
- **customer.py**: Defines the `Customer` entity class and its properties.
- **login_cache.py**: Manages login-related caching to enhance performance.
- **order.py**: Defines the `Order` entity class and its properties.
### enum_entity

- **init.py**: Initializes the `enum_entity` module.
- **car_make.py**: Defines enumerations for car makes.
- **car_model.py**: Defines enumerations for car models.
- **coupon_status.py**: Defines enumerations for coupon statuses.
- **message.py**: Contains enumerations for various system messages.
- **order_status.py**: Defines enumerations for order statuses.
### exception

- **init.py**: Initializes the `exception` module.
- **duplicated_exception.py**: Custom exception class for handling duplicate records or entries.
### main.py

- **main.py**: The entry point of the application, where the main logic is executed to start the car rental system.
### main.spec

- **main.spec**: A configuration file for packaging the application, possibly using PyInstaller.
### menu

- **init.py**: Initializes the `menu` module.
- **admin_menu.py**: Defines the admin menu interface and navigation logic.
- **customer_menu.py**: Defines the customer menu interface and navigation logic.
- **decorator**: Contains decorators used to enhance menu functionalities:
   - **init.py**: Initializes the `decorator` submodule.
   - **base_menu_decorator.py**: Base decorator class for menus.
   - **head_foot_decorator.py**: Adds headers and footers to menu displays.
- **main_menu.py**: Defines the main menu interface for the application.
### requirements.txt

- **requirements.txt**: Lists all Python dependencies required to run the project.
### schema

- **init.py**: Initializes the `schema` module.
- **initial_db.py**: Contains scripts or logic to initialize and set up the database schema for the first time.
### service

- **init.py**: Initializes the `service` module.
- **admin**: Contains service classes for admin operations:
   - **init.py**: Initializes the `admin` submodule.
   - **admin_car_service.py**: Provides business logic for car management by admins.
   - **admin_coupon_service.py**: Provides business logic for coupon management by admins.
   - **admin_login_service.py**: Manages admin login logic.
   - **admin_order_service.py**: Handles order management logic for admins.
   - **admin_registration_service.py**: Manages admin registration logic.
- **customer**: Contains service classes for customer operations:
   - **init.py**: Initializes the `customer` submodule.
   - **customer_car_service.py**: Provides business logic for car selection and management by customers.
   - **customer_coupon_service.py**: Handles coupon-related business logic for customers.
   - **customer_login_service.py**: Manages customer login logic.
   - **customer_order_service.py**: Handles order management logic for customers.
   - **customer_registration_service.py**: Manages customer registration logic.
### utils

- **init.py**: Initializes the `utils` module.
- **check_if_duplicated.py**: Utility script to check for duplicate records in the database.
- **connect_db.py**: Provides functions to establish and manage database connections.
- **convert_date_format.py**: Contains utility functions to convert date formats.
- **fee_caculation.py**: Utility for calculating rental fees and related charges.
- **generate_id.py**: Provides functions to generate unique identifiers for various entities.
- **input_format_verification.py**: Contains functions to verify and validate user input formats.
- **release_db.py**: Utility script for releasing or closing database connections.
## **Known Issues**

- **Password**: **No secure solution to handle password.
- **Registration**: **Basic validation rules are applied for user_name and password, no validation machenism for other fields like license no, phone or branch code etc.
- **Delete car**: System doesn't validate related orders while admin deletes a car.
- **Book rental**: **System doesn't apply locker mechanism for booking, it may cause issues while large number of customers use system simultaneously.

We are actively working on resolving these issues and welcome contributions and feedback from the community.
## **Contributing**
We welcome contributions to enhance the **CX Car Rental System**. Please fork the repository, create a new branch for your feature or bug fix, and submit a pull request with a detailed description of your changes.
## **License**
Distributed under the MIT License. See LICENSE.txt for more information.
## **Credits**
- **Developer**: Peter (Chi Xu) 
- **Role**: Lead Software Developer
- **Contributions:** Overall design, development, and maintenance of the project, including design the system architecture, develop core functionalities and integrate the user interface with the backend.
## Contact
- **Email**: xuchi007@hotmail.com
- **Project Link**: [https://github.com/xc840122/cx_car_rental_system](https://github.com/xc840122/cx_car_rental_system/tree/main)

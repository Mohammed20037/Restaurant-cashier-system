# Professional Restaurant Cashier System - README

![image](https://github.com/Mohammed20037/Restaurant-cashier-system/assets/113844625/0861b398-2998-42b0-a4f3-9f80dd74f4cc)


## Introduction

The Professional Restaurant Cashier System is a powerful and versatile Python-based application designed to streamline the restaurant management process. It provides a user-friendly graphical interface for restaurant staff to manage orders, calculate bills, and generate detailed receipts. This README will guide you through setting up the system and using its features effectively.

## Table of Contents

1. [Getting Started](#getting-started)
   - [Database Setup](#database-setup)
   - [Python Environment](#python-environment)
2. [System Features](#system-features)
   - [Dish Management](#dish-management)
   - [Order Handling](#order-handling)
   - [Billing and Receipts](#billing-and-receipts)
3. [Usage Guide](#usage-guide)
4. [Contributing](#contributing)
5. [License](#license)

## 1. Getting Started

### Database Setup

Before using the Restaurant Cashier System, you need to set up the MySQL database and populate it with essential tables and data. Below are the SQL commands to create the necessary database and tables:

```sql
CREATE DATABASE restaurant_inventory;

USE restaurant_inventory;

-- Create tables for ingredients, dishes, recipe, and orders
-- (Insert your SQL statements here, as provided in your code)

-- Insert sample data for dishes and ingredients
-- (Insert your SQL statements here, as provided in your code)
```

Please replace `(Insert your SQL statements here, as provided in your code)` with the actual SQL statements from your code.

### Python Environment

Ensure that you have the required Python libraries installed. You can install them using `pip`:

```bash
pip install mysql-connector-python
```

## 2. System Features

### Dish Management

- **Dish Catalog:** View a catalog of available dishes, including names, descriptions, and prices.
- **Add to Cart:** Add dishes to the cart with specified quantities.
- **Duplicate Handling:** Automatically handles duplicates to simplify order management.

### Order Handling

- **Order Summary:** View a summary of the selected dishes and their quantities in the cart.
- **Clear Cart:** Start a new order by clearing the cart.

### Billing and Receipts

- **Bill Calculation:** Automatically calculates the total cost of selected dishes, including tax.
- **Receipt Generation:** Generate detailed receipts with itemized dish information.

## 3. Usage Guide

1. Run the Python script that contains the provided code.

2. The system's graphical user interface (GUI) will open, displaying the catalog of available dishes.

3. To add a dish to the cart:
   - Enter the dish's ID and the desired quantity in the input fields.
   - Click the "Add to Cart" button.
   - The selected dish will appear in the cart display.

4. Continue adding dishes to the cart as needed.

5. To calculate the bill and generate a receipt:
   - Click the "Generate Receipt" button.
   - The receipt will display the selected dishes, quantities, individual prices, total cost, and tax.

6. To start a new order and clear the cart:
   - Click the "New Order" button.

## 4. Contributing

We welcome contributions to improve and enhance the Restaurant Cashier System. If you have ideas for new features, bug fixes, or other improvements, please consider contributing by creating a pull request or opening an issue in the project repository.

## 5. License

The Professional Restaurant Cashier System is distributed under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the terms of the license.

Feel free to reach out if you encounter any issues or have suggestions for further improvements. Enjoy using the Professional Restaurant Cashier System!

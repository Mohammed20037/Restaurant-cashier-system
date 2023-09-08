import mysql.connector
from tkinter import *
from tkinter import ttk
from decimal import Decimal

# Connect to the MySQL database
db = mysql.connector.connect(
    host="",
    user="",
    password="PUT_YOUR_PASSWORD",
    database="restaurant_inventory"
)

# Get a cursor object (fetch data from the database) 
cursor = db.cursor()

# Fetch all the rows from the dishes table
cursor.execute("SELECT * FROM dishes")
rows = cursor.fetchall()

# Create a new window
window = Tk()
window.title("NSMM Restaurant")
window.geometry("1110x500")
window.configure(bg="#F0F0F0")  # Set background color
window.iconbitmap("C:/Users/medoh/OneDrive/Desktop/logo.ico.ico")  # Set the window icon

# Create a Treeview widget
tree = ttk.Treeview(window)
tree["columns"] = ("ID", "Name", "Description", "Price")

# Define column headings
tree.heading("#0", text="")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Description", text="Description")
tree.heading("Price", text="Price")

# Create a dictionary to keep track of duplicate dishes
dish_set = set()

# Add data to the treeview
for row in rows:
    # Skip duplicate dishes
    if row[1] in dish_set:
        continue

    # Get the dish information
    dish_id = row[0]
    dish_name = row[1]
    dish_price = row[2]
    dish_description = row[3]

    # Handle empty description and incorrect placement of price
    if not dish_description:
        dish_description = dish_price
        dish_price = ""

    # Insert the row into the treeview
    tree.insert("", "end", text="", values=(dish_id, dish_name, dish_price, dish_description))

    # Add the dish to the dish set
    dish_set.add(dish_name)

# Configure column properties
tree.column("#0", width=0, stretch=NO)
tree.column("ID", anchor=CENTER, width=80)
tree.column("Name", anchor=W, width=200)
tree.column("Price", anchor=CENTER, width=100)
tree.column("Description", anchor=W, width=400)

# Add a vertical scrollbar to the treeview
scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)

# Pack the treeview and scrollbar
tree.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

# Initialize the cart
cart = {}

# Define a function to add a dish to the cart
def add_to_cart():
    # Get the ID and quantity of the dish from the user
    selected_dish_id = int(input_id.get())
    selected_dish_quantity = int(input_quantity.get())

    # Create a new connection and cursor object
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="restaurant_inventory"
    )
    cursor = db_connection.cursor()

    # Execute a SELECT statement to fetch the selected dish from the table
    cursor.execute(f"SELECT * FROM dishes WHERE id = {selected_dish_id}")

    # Fetch the row returned by the SELECT statement
    selected_dish = cursor.fetchone()

    # Add the selected dish to the cart
    cart[selected_dish[1]] = selected_dish_quantity

    # Clear the inputs
    input_id.delete(0, END)
    input_quantity.delete(0, END)

    # Update the cart display
    update_cart_display()

    # Update the total cost display
    update_total_cost_display()

    # Close the cursor and connection
    cursor.close()
    db_connection.close()

# Define a function to update the cart display
def update_cart_display():
    # Clear the current cart display
    cart_label.config(text="")

    # Add each item in the cart to the cart display
    for dish, quantity in cart.items():
        cart_label.config(text=cart_label.cget("text") + f"{dish}: {quantity}\n")

# Define a function to update the total cost display
def update_total_cost_display():
    # Calculate the total cost of all dishes in the cart
    total_cost = calculate_total_cost()

    # Calculate the tax
    tax_rate = 0.07
    tax = total_cost * tax_rate

    # Update the total cost display
    total_cost_label.config(text=f"Total cost: ${total_cost:.2f} (Tax: ${tax:.2f})")

    # Store the total cost and tax as global variables
    global total_cost_value, tax_value
    total_cost_value = total_cost
    tax_value = tax

# Define a helper function to fetch the price of a dish from the database
def get_dish_price(dish):
    cursor.execute(f"SELECT price FROM dishes WHERE name = '{dish}'")
    price = cursor.fetchone()[0]  # Assuming the price column is in index 0
    cursor.fetchall()  # Consume and discard unread result
    return price

# Define a function to calculate the total cost of all dishes in the cart
def calculate_total_cost():
    total_cost = sum([quantity * get_dish_price(dish) for dish, quantity in cart.items()])
    return total_cost

# Define a function to clear the cart and start a new order
def clear_cart():
    cart.clear()
    update_cart_display()
    update_total_cost_display()

# Define a function to generate the receipt
def generate_receipt():
    # Calculate the total cost of all dishes in the cart
    total_cost = sum([quantity * get_dish_price(dish) for dish, quantity in cart.items()])

    # Calculate the tax
    tax_rate = Decimal('0.07')
    tax = total_cost * tax_rate

    # Convert total_cost to float
    total_cost = float(total_cost)

    # Add the tax to the total cost
    total_cost += float(tax)

    # Create a new window for the receipt
    receipt_window = Tk()
    receipt_window.title("Receipt")
    receipt_window.geometry("400x400")
    receipt_window.configure(bg="white")

    # Create a text widget for the receipt
    receipt_text = Text(receipt_window, font=("Helvetica", 12), bg="white", fg="black")
    receipt_text.pack(padx=20, pady=20)

    # Add the chosen dishes and their quantities to the receipt text
    for dish, quantity in cart.items():
        price = get_dish_price(dish) * quantity  # Calculate price based on quantity
        receipt_text.insert(END, f"{dish}\t{quantity}\t${price:.2f}\n")

    # Add a separator to the receipt text
    receipt_text.insert(END, "-" * 30 + "\n")

    # Add the total cost to the receipt text
    receipt_text.insert(END, f"Total cost:\t\t${total_cost:.2f} (Tax: ${tax:.2f})\n")

    # Disable editing in the receipt text widget
    receipt_text.configure(state='disabled')

    # Run the main loop of the receipt window
    receipt_window.mainloop()

# Create labels and entry fields for dish ID and quantity
id_label = Label(window, text="Dish ID:", bg="#F0F0F0", font=("Arial", 12))  # Set background color and font
id_label.pack(pady=10)

input_id = Entry(window, font=("Arial", 12))  # Set font
input_id.pack()

quantity_label = Label(window, text="Quantity:", bg="#F0F0F0", font=("Arial", 12))  # Set background color and font
quantity_label.pack(pady=10)

input_quantity = Entry(window, font=("Arial", 12))  # Set font
input_quantity.pack()

# Create a button to add a dish to the cart
add_to_cart_button = Button(window, text="Add to Cart", command=add_to_cart, font=("Arial", 12), bg="#008000", fg="white")  # Set font and colors
add_to_cart_button.pack(pady=10)

# Create a label to display the cart
cart_label = Label(window, text="", bg="#F0F0F0", font=("Arial", 12), justify=LEFT)  # Set background color, font, and alignment
cart_label.pack(pady=10)

# Create a button to generate the receipt
generate_receipt_button = Button(window, text="Generate Receipt", command=generate_receipt, font=("Arial", 12), bg="#FF4500", fg="white")  # Set font and colors
generate_receipt_button.pack(pady=10)

# Create a button to clear the cart and start a new order
clear_cart_button = Button(window, text="New Order", command=clear_cart, font=("Arial", 12), bg="#FF0000", fg="white")  # Set font and colors
clear_cart_button.pack(pady=10)

# Create a label to display the total cost
total_cost_label = Label(window, text="", bg="#F0F0F0", font=("Arial", 12))  # Set background color and font
total_cost_label.pack(pady=10)

# Set the window icon
window.iconbitmap(r'C:\Users\medoh\OneDrive\Desktop\logo.ico.ico')

# Run the main loop of the window
window.mainloop()

# Close the cursor and database connection
cursor.close()
db.close()

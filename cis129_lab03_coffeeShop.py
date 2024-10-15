# ----------------------------------------
# cis129_lab03_coffeeShop.py
# Author: N ARIF
# Date: 10/15/24
# Description: This program calculates the total cost of coffee and muffins purchased
#              by the user, including a 6% sales tax, and displays a formatted receipt.
# ----------------------------------------

# Prices of items
coffee_price = 5.0  # Price of a single coffee
muffin_price = 4.0   # Price of a single muffin
tax_rate = 0.06      # Sales tax rate

# Print shop header
print("***************************************")
print("My Coffee and Muffin Shop")

# Get user input for number of coffees and muffins
num_coffees = int(input("Number of coffees bought?\n"))
num_muffins = int(input("Number of muffins bought?\n"))

# Print separator for receipt
print("***************************************")

# Calculate subtotal for coffees and muffins
subtotal_coffees = num_coffees * coffee_price  # Total cost of coffees
subtotal_muffins = num_muffins * muffin_price    # Total cost of muffins
subtotal = subtotal_coffees + subtotal_muffins    # Combined subtotal

# Calculate tax based on subtotal
tax = subtotal * tax_rate  # Sales tax calculation

# Calculate the total amount due
total = subtotal + tax  # Final total including tax

# Print receipt header
print("My Coffee and Muffin Shop Receipt")
# Print detailed itemized costs
print(f"{num_coffees} Coffee at ${coffee_price} each: ${subtotal_coffees:.2f}")
print(f"{num_muffins} Muffins at ${muffin_price} each: ${subtotal_muffins:.2f}")
print(f"6% tax: ${tax:.2f}")  # Display the calculated tax
print("---------")  # Separator line for clarity
print(f"Total: ${total:.2f}")  # Final total amount due

# Print footer to complete the receipt
print("***************************************")

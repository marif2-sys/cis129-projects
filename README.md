# cis129-projects

# ----------------------------------------
# cis129_lab03_coffeeShop.py
# Author: N ARIF 
# Date: 10/15/24
# Description: This program calculates the total cost of coffee, muffins,
#              croissants, and tea purchased by the user, including a 6% sales tax,
#              and displays a formatted receipt with a thank-you message.
# ----------------------------------------

# Prices of items
coffee_price = 5.0    # Price of a single coffee
muffin_price = 4.0     # Price of a single muffin
croissant_price = 3.5  # Price of a single croissant
tea_price = 2.0        # Price of a single tea
tax_rate = 0.06        # Sales tax rate

# Print shop header
print("***************************************")
print("My Cozy Coffee and Muffin Shop")

# Get user input for number of coffees, muffins, croissants, and tea
num_coffees = int(input("Number of coffees bought?\n"))
num_muffins = int(input("Number of muffins bought?\n"))
num_croissants = int(input("Number of croissants bought?\n"))
num_tea = int(input("Number of tea bought?\n"))

# Print separator for receipt
print("***************************************")

# Calculate subtotal for each item
subtotal_coffees = num_coffees * coffee_price
subtotal_muffins = num_muffins * muffin_price
subtotal_croissants = num_croissants * croissant_price
subtotal_tea = num_tea * tea_price
subtotal = (subtotal_coffees + subtotal_muffins + 
            subtotal_croissants + subtotal_tea)  # Combined subtotal

# Calculate tax based on subtotal
tax = subtotal * tax_rate  # Sales tax calculation

# Calculate the total amount due
total = subtotal + tax  # Final total including tax

# Print receipt header
print("My Cozy Coffee and Muffin Shop Receipt")
# Print detailed itemized costs
if num_coffees > 0:
    print(f"{num_coffees} Coffee at ${coffee_price} each: ${subtotal_coffees:.2f}")
if num_muffins > 0:
    print(f"{num_muffins} Muffins at ${muffin_price} each: ${subtotal_muffins:.2f}")
if num_croissants > 0:
    print(f"{num_croissants} Croissants at ${croissant_price} each: ${subtotal_croissants:.2f}")
if num_tea > 0:
    print(f"{num_tea} Tea at ${tea_price} each: ${subtotal_tea:.2f}")

print(f"6% tax: ${tax:.2f}")  # Display the calculated tax
print("---------")  # Separator line for clarity
print(f"Total: ${total:.2f}")  # Final total amount due

# Thank you message
print("Thank you for visiting My Cozy Coffee and Muffin Shop!")
print("We hope to see you again soon!")
# Print footer to complete the receipt
print("***************************************")

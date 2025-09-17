# Adding In The Catalog

# Lovely Loveseat Description and Price
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

# Stylish Settee Description and Price
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

# Luxurious Lamp Description and Price
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

# Sales Tax
sales_tax = 0.088

# Customer One Variables
customer_one_total = 0
customer_one_itemization = ""

# Customer One Makes Purchases

# Customer buys the Lovely Loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description + "\n"

# Customer buys the Luxurious Lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description + "\n"

# Calculate Sales Tax
customer_one_tax = customer_one_total * sales_tax

# Add Sales Tax to Total
customer_one_total += customer_one_tax

# Print the Receipt
print("Customer One Items:")
print(customer_one_itemization)

print("Customer One Total:")
print(f"${customer_one_total:.2f}")  # Format the total to 2 decimal places

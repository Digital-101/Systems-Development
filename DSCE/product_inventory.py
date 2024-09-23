# Input list of tuples
inventory = [
    (101, 'Laptop', 15),
    (102, 'Mouse', 35),
    (103, 'Keyboard', 20),
    (101, 'Laptop', 5),
    (102, 'Mouse', 10)
]

# Initialize an empty dictionary to store product details
product_inventory = {}

# Process each tuple in the list
for product_id, name, quantity in inventory:
    if product_id in product_inventory:
        existing_name, existing_quantity = product_inventory[product_id]
        if name == existing_name:  # Logical check to ensure product name matches
            product_inventory[product_id] = (name, existing_quantity + quantity)
    else:
        product_inventory[product_id] = (name, quantity)

print(product_inventory)

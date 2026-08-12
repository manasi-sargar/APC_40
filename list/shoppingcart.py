cart = ["Milk", "Bread", "Apple"]

# Add item
cart.append("Rice")

# Remove item
cart.remove("Bread")

# Search item
if "Apple" in cart:
    print("Apple is available")
else:
    print("Apple is not available")

# Display cart
print("Shopping cart:", cart)

# Count items
print("Total items:", len(cart))
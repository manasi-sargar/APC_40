products = [
    ("Laptop", 50000, 1),
    ("Mouse", 500, 3),
    ("Keyboard", 1500, 2)
]
values = list(map(
    lambda x: (x[0], x[1] * x[2]),
    products
))
print("Total values:", values)
expensive = list(filter(
    lambda x: x[1] > 1000,
    products
))
print("Above 1000:", expensive)
sorted_products = sorted(
    values,
    key=lambda x: x[1]
)
print("Sorted:", sorted_products)
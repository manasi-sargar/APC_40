employees = [
    ("Amit", 30000),
    ("Rahul", 50000),
    ("Sneha", 40000)
]
result = sorted(employees, key=lambda x: x[1])
print(result)
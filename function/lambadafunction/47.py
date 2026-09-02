students = [
    ("Amit", 70),
    ("Rahul", 90),
    ("Sneha", 80)
]
result = sorted(students, key=lambda x: x[1])
print(result)
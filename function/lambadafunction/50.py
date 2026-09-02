employees = [
    ("Amit", "IT", 45000),
    ("Rahul", "HR", 60000),
    ("Sneha", "IT", 70000)
]
high_salary = list(filter(lambda x: x[2] > 50000, employees))
print("Above 50000:", high_salary)
increased = list(map(
    lambda x: (x[0], x[1], x[2] * 1.10),
    employees
))
print("Increased:", increased)
sorted_emp = sorted(employees, key=lambda x: x[2])
print("Sorted:", sorted_emp)
students = [
    ("Amit", 70),
    ("Rahul", 90),
    ("Sneha", 80)
]
average = sum(map(lambda x: x[1], students)) / len(students)
print("Average =", average)
above_75 = list(filter(lambda x: x[1] > 75, students))
print("Above 75 =", above_75)
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted =", sorted_students)
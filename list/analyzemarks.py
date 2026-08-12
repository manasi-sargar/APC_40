marks = [
    85, 72, 90, 65, 78,
    88, 92, 55, 70, 81,
    76, 95, 68, 84, 73,
    60, 89, 77, 91, 69
]
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)
above_average = 0
below_average = 0
for mark in marks:
    if mark > average:
        above_average += 1
    elif mark < average:
        below_average += 1
print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students above average:", above_average)
print("Students below average:", below_average)
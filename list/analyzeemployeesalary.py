salaries = [25000, 35000, 55000, 60000, 28000, 45000, 75000, 52000]

highest = max(salaries)
lowest = min(salaries)
average = sum(salaries) / len(salaries)

above_50000 = 0
below_30000 = 0

for salary in salaries:
    if salary > 50000:
        above_50000 += 1

    if salary < 30000:
        below_30000 += 1

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("Employees earning above ₹50,000:", above_50000)
print("Employees earning below ₹30,000:", below_30000)
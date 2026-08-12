students = ["Manasi", "Priya", "Rahul", "Sneha"]

# Total students
print("Total students:", len(students))

# Search student
name = "Priya"

if name in students:
    print(name, "is present")
else:
    print(name, "is absent")

# Add new student
students.append("Amit")

# Remove absent student
students.remove("Rahul")

print("Updated student list:", students)
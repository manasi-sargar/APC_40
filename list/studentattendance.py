students = ["Manasi", "Priya", "Rahul", "Sneha"]
print("Total students:", len(students))
name = "Priya"
if name in students:
    print(name, "is present")
else:
    print(name, "is absent")
students.append("Amit")
students.remove("Rahul")
print("Updated student list:", students)
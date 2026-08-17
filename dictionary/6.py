employees={101:"Rahul",102:"Amit",103:"Sneha",104:"Priya"}
id=int(input("Enter employee ID: "))
if id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")
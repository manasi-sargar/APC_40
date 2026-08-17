students={"Amit":75,"Rahul":88,"Sneha":95}
students["Priya"]=82
students["Rahul"]=90
del students["Amit"]
name=input("Enter student name to search: ")
if name in students:
    print("Student found:",students[name])
else:
    print("Student not found")
print("All students:",students)
highest=max(students,key=students.get)
print("Highest marks:",highest,students[highest])
average=sum(students.values())/len(students)
print("Average marks:",average)
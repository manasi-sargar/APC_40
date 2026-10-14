import re
s=input("Enter student details (Name: Rahul, Roll: 12, Marks: 85): ")
p=r'Name:\s*([A-Za-z ]+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)'
m=re.findall(p,s)
for name,roll,marks in m:
 print("Name:",name.strip())
 print("Roll Number:",roll)
 print("Marks:",marks)
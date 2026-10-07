#write python code to analyze data and find the heighest salary,avarage salary,and department-wise salary
data = [
    ("Manasi", "IT", 50000),
    ("Kanishka", "HR", 40000),
    ("Arpita", "IT", 60000),
    ("Sakshi", "HR", 45000)
]
salaries = [x[2] for x in data]
print("Highest Salary:", max(salaries))
print("Average Salary:", sum(salaries) / len(salaries))
dept = {}
for name, d, salary in data:
    dept[d] = dept.get(d, 0) + salary
print("Department-wise Salary:", dept)

students={"Amit":"CSE","Rahul":"IT","Sneha":"CSE","Priya":"ENTC","Rohit":"IT"}
departments={}
for name,department in students.items():
    if department not in departments:
        departments[department]=[]
    departments[department].append(name)
print(departments)
patients = (
    (101, "Manasi", 20, "A+"),
    (102, "Priya", 22, "B+"),
    (103, "Rahul", 25, "A+")
)
print("All Patient Records:")

for patient in patients:
    print(patient)
search_id = 102

for patient in patients:
    if patient[0] == search_id:
        print("Patient found:", patient)
print("Total patients:", len(patients))
print("Patients with A+ blood group:")
for patient in patients:
    if patient[3] == "A+":
        print(patient)
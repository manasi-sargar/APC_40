patients = [
    ["Manasi", 20],
    ["Priya", 22],
    ["Rahul", 25]
]

# Add a patient
patients.append(["Sneha", 21])

# Delete a patient
patients.remove(["Rahul", 25])

# Search a patient
name = "Priya"

found = False

for patient in patients:
    if patient[0] == name:
        print("Patient found")
        print("Name:", patient[0])
        print("Age:", patient[1])
        found = True

if not found:
    print("Patient not found")

# Display all patients
print("\nAll patients:")

for patient in patients:
    print("Name:", patient[0], "Age:", patient[1])

# Count patients
print("Total patients:", len(patients))
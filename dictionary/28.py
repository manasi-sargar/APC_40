contacts={"Amit":"9876543210","Rahul":"9876543211","Sneha":"9876543212"}
contacts["Priya"]="9876543213"
name=input("Enter contact to search: ")
if name in contacts:
    print("Phone number:",contacts[name])
else:
    print("Contact not found")
contacts["Amit"]="9999999999"
del contacts["Rahul"]
print("All contacts:",contacts)
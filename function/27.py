def consultation():
    return 500
def laboratory():
    return 1000
def medicine():
    return 1500
def room():
    return 2000
def final_bill(category):
    total = consultation() + laboratory() + medicine() + room()
    if category == "senior":
        total = total * 0.90
    return total
category = input("Enter category: ")
print("Final Bill =", final_bill(category))
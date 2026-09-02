def electricity_bill(units):
    if units <= 100:
        amount = units * 5
    elif units <= 200:
        amount = 500 + (units - 100) * 7
    else:
        amount = 1200 + (units - 200) * 10
    fixed = 100
    tax = amount * 0.05
    return amount + fixed + tax
units = int(input("Enter units: "))
print("Final Bill =", electricity_bill(units))
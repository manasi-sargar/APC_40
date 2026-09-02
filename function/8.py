#8.	Create a function power(base, exponent) to calculate the value of base raised to exponent.
def power(base, exponent):
    return base ** exponent
b=int(input("enter base: "))
e=int(input("enter exponent:"))
print("Answer: ",power(b,e))
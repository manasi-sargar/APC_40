#3.	Define a function that accepts two numbers and returns the greater number.
def greater(a, b):
    if a > b:
        return a
    else:
        return b
a=int(input("enter first number: "))
b=int(input("enter second number: "))
print("greater: ",greater(a, b))
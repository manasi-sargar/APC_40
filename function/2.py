#2.	Write a function check_even_odd(n) that determines whether a given number is even or odd.
def check_even_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "odd"
n=int(input("enter number: "))
print(check_even_odd(n))
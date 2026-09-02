#7.	Write a function that accepts n and returns the sum of the first n natural numbers.
def natural_sum(n):
    return n * (n + 1) // 2
n=int(input("enter number n :"))
print(natural_sum(n))
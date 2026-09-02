#13.	Write a function that accepts a list of numbers and returns their average.
def average(numbers):
    return sum(numbers) / len(numbers)
numbers=list(map(int,input("enter numbers: ")))
print("Average =", average(numbers))

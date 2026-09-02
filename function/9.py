#9.	Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.
def largest(numbers):
    large = numbers[0]
    for n in numbers:
        if n > large:
            large = n
    return large
numbers = list(map(int, input("Enter numbers: ").split()))
print("Largest =", largest(numbers))
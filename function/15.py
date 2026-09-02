#15.	Write a function that accepts a list and returns a new list containing only unique elements.
def unique(numbers):
    result = []
    for n in numbers:
        if n not in result:
            result.append(n)
    return result
numbers = list(map(int, input("Enter numbers: ").split()))
print(unique(numbers))

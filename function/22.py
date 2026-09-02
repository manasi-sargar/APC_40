
def calculate(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    return minimum, maximum, total, average
numbers = list(map(int, input("Enter numbers: ").split()))
a, b, c, d = calculate(numbers)
print("Minimum =", a)
print("Maximum =", b)
print("Sum =", c)
print("Average =", d)
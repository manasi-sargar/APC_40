def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[-2]
numbers = list(map(int, input("Enter numbers: ").split()))
print("Second largest =", second_largest(numbers))

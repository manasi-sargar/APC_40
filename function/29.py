def binary_search(numbers, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if numbers[mid] == key:
        return mid
    elif key < numbers[mid]:
        return binary_search(numbers, key, low, mid - 1)
    else:
        return binary_search(numbers, key, mid + 1, high)
numbers = [10, 20, 30, 40, 50]
key = int(input("Enter number: "))
print(binary_search(numbers, key, 0, len(numbers) - 1))
numbers = [10, 20, 30, 40, 50]

# Left rotation
left = numbers[1:] + numbers[:1]

# Right rotation
right = numbers[-1:] + numbers[:-1]

print("Original list:", numbers)
print("Left rotation:", left)
print("Right rotation:", right)
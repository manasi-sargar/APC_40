numbers = []

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Ascending order:", ascending)
print("Descending order:", descending)
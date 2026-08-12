numbers = []
for i in range(15):
    n = int(input("Enter number: "))
    numbers.append(n)
even = 0
odd = 0
for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)
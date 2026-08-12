numbers = (10, 20, 10, 30, 20, 10, 40)
for number in numbers:
    if numbers.index(number) == numbers.index(number):
        print(number, ":", numbers.count(number))
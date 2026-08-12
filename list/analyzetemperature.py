temperatures = [
    30, 32, 29, 35, 31,
    28, 33, 36, 30, 27,
    34, 31, 29, 37, 32,
    30, 28, 35, 33, 31,
    29, 36, 34, 30, 27,
    32, 35, 31, 33, 29
]
hottest = max(temperatures)
coldest = min(temperatures)
average = sum(temperatures) / len(temperatures)
above_average = 0
below_average = 0
for temperature in temperatures:
    if temperature > average:
        above_average += 1
    elif temperature < average:
        below_average += 1
print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above_average)
print("Days below average:", below_average)
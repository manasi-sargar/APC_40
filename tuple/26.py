tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)
common = ()
for number in tuple1:
    if number in tuple2:
        common = common + (number,)
print("Common elements:", common)
tuple1 = (10, 20, 30)
tuple2 = (20, 30, 40, 50)
merged = tuple1 + tuple2
unique = ()
for number in merged:
    if number not in unique:
        unique = unique + (number,)
print("Merged tuple:", merged)
print("After removing duplicates:", unique)
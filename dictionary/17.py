dict1={"a":1,"b":2,"c":3}
dict2={"b":4,"c":5,"d":6}
common=set(dict1.keys())&set(dict2.keys())
print("Common keys:",common)
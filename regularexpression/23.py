import re
s=input("Enter Python code: ")
print(re.findall(r'^\s*#.*$',s,re.M))
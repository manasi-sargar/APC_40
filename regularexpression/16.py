import re
s=input("Enter password: ")
p=r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}'
if re.fullmatch(p,s):
 print("Valid password")
else:
 print("Invalid password")
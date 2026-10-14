import re
s=input("Enter vehicle number: ")
if re.fullmatch(r'[A-Z]{2}\d{2}[A-Z]{1,3}\d{4}',s.upper()):
 print("Valid vehicle number")
else:
 print("Invalid vehicle number")
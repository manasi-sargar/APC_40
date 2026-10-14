import re
s=input("Enter product code: ")
if re.fullmatch(r'[A-Z]{3}-\d{4}-[A-Z]{2}',s):
 print("Valid product code")
else:
 print("Invalid product code")
import re
s=input("Enter email address: ")
if re.fullmatch(r'[\w.+-]+@[\w-]+(?:\.[\w-]+)+',s):
 print("Valid email")
else:
 print("Invalid email")
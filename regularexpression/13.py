import re
s=input("Enter a paragraph: ")
print(re.findall(r'\b(?:0[1-9]|[12]\d|3[01])-(?:0[1-9]|1[0-2])-\d{4}\b',s))
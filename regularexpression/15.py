import re
s=input("Enter a post: ")
print(re.findall(r'#[A-Za-z0-9_]+',s))
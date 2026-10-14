import re
s=input("Enter text (use \\t for tab and \\n for newline): ")
s=s.replace('\\t','\t').replace('\\n','\n')
print(re.findall(r'[ \t\n]',s))
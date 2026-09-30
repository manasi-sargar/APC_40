import pandas as pd
salary={"A":45000,"B":60000,"C":75000,"D":50000,"E":65000}
s=pd.Series(salary)
print(s)
print("Highest salary:",s.max())
print("Lowest salary:",s.min())
print("Average salary:",s.mean())
print("Employees earning above 50000:")
print(s[s>50000])
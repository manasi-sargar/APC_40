import pandas as pd
data={"Employee_ID":[101,102,103,104,105],"Employee_Name":["A","B","C","D","E"],"Department":["CSE","IT","CSE","HR","IT"],"Salary":[45000,60000,75000,50000,65000],"Experience":[2,5,7,4,6]}
df=pd.DataFrame(data)
print("Salary greater than 50000:")
print(df[df["Salary"]>50000])
print("Average salary:",df["Salary"].mean())
print("Highest salary:",df["Salary"].max())
print("Highest experience:")
print(df.loc[df["Experience"].idxmax()])
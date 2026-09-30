import pandas as pd
data={"Student_ID":[1,2,3,4,5],"Student_Name":["A","B","C","D","E"],"Python":[80,70,90,60,85],"DBMS":[75,80,88,65,90],"Mathematics":[85,72,95,70,80]}
df=pd.DataFrame(data)
df["Total"]=df[["Python","DBMS","Mathematics"]].sum(axis=1)
df["Average"]=df[["Python","DBMS","Mathematics"]].mean(axis=1)
print(df)
print("Students above 75 average:")
print(df[df["Average"]>75])
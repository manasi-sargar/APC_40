import pandas as pd
data={"Student_ID":[1,2,3,4,5],"Name":["A","B","C","D","E"],"Department":["CSE","IT","CSE","ECE","CSE"],"Total_Classes":[100,100,100,100,100],"Classes_Attended":[80,70,90,65,75]}
df=pd.DataFrame(data)
df["Attendance_Percentage"]=df["Classes_Attended"]/df["Total_Classes"]*100
print(df)
print("Students below 75%:")
print(df[df["Attendance_Percentage"]<75])
import pandas as pd
data={"Patient_ID":[1,2,3,4,5],"Patient_Name":["A","B","C","D","E"],"Age":[65,45,70,30,80],"Disease":["Diabetes","Fever","Heart","Cold","Cancer"],"Medical_Charges":[60000,20000,80000,15000,90000]}
df=pd.DataFrame(data)
print("Patients above 60:")
print(df[df["Age"]>60])
print("Average medical charge:",df["Medical_Charges"].mean())
print("Maximum medical charge:",df["Medical_Charges"].max())
print("Charges greater than 50000:")
print(df[df["Medical_Charges"]>50000])
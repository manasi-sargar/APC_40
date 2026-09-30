import pandas as pd
data={"Product_ID":[1,2,3,4,5],"Product_Name":["Laptop","Phone","TV","Mouse","Keyboard"],"Category":["Electronics","Electronics","Electronics","Accessory","Accessory"],"Price":[50000,30000,40000,1000,2000],"Quantity":[2,3,1,15,10]}
df=pd.DataFrame(data)
df["Total_Sales"]=df["Price"]*df["Quantity"]
print(df)
print("Sales greater than 10000:")
print(df[df["Total_Sales"]>10000])
print("Maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])
print("Average sales:",df["Total_Sales"].mean())
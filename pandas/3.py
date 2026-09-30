import pandas as pd
data={"Product_ID":[1,2,3,4,5],"Product_Name":["Laptop","Phone","Tablet","Mouse","Keyboard"],"Category":["Electronics","Electronics","Electronics","Accessory","Accessory"],"Price":[50000,30000,20000,1000,2000],"Quantity":[2,3,4,10,8]}
df=pd.DataFrame(data)
df["Total_Amount"]=df["Price"]*df["Quantity"]
print(df)
print("Highest sales:")
print(df.loc[df["Total_Amount"].idxmax()])
import pandas as pd
data={"Order_ID":[1,2,3,4,5],"Customer":["A","B","C","D","E"],"Product":["Laptop","Phone","Tablet","Mouse","Keyboard"],"Quantity":[1,2,3,5,10],"Price":[50000,30000,20000,1000,2000],"Discount":[2000,1000,500,100,200]}
df=pd.DataFrame(data)
df["Final_Amount"]=df["Quantity"]*df["Price"]-df["Discount"]
print("All orders:")
print(df)
print("Orders above 5000:")
print(df[df["Final_Amount"]>5000])
print("Highest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])
print("Average order value:",df["Final_Amount"].mean())
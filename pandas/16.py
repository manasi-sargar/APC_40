import pandas as pd
df=pd.read_csv("weather.csv")
print("Maximum temperature:",df["Temperature"].max())
print("Minimum temperature:",df["Temperature"].min())
print("Average temperature:",df["Temperature"].mean())
print("Temperature above 35:")
print(df[df["Temperature"]>35])
print("City-wise average temperature:")
print(df.groupby("City")["Temperature"].mean())
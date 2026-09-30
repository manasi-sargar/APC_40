import pandas as pd
prices={"Laptop":50000,"Phone":30000,"Tablet":20000,"Mouse":1000,"Keyboard":2000}
s=pd.Series(prices)
print(s)
s=s*1.10
print("Prices after 10% increase:")
print(s)
print("Most expensive product:")
print(s.idxmax(),s.max())
print("Products above 1000:")
print(s[s>1000])
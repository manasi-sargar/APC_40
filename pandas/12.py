import pandas as pd
attendance={"A":80,"B":70,"C":95,"D":65,"E":92}
s=pd.Series(attendance)
print(s)
print("Average attendance:",s.mean())
print("Below 75%:")
print(s[s<75])
print("Above 90%:")
print(s[s>90])
print("Highest attendance:",s.max())
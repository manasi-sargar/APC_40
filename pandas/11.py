import pandas as pd
ages={101:65,102:45,103:70,104:30,105:80}
s=pd.Series(ages)
print(s)
print("Average age:",s.mean())
print("Oldest patient:",s.idxmax(),s.max())
print("Youngest patient:",s.idxmin(),s.min())
print("Patients above 60:")
print(s[s>60])
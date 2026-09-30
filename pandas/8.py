import pandas as pd
marks={"A":80,"B":70,"C":90,"D":65,"E":85}
s=pd.Series(marks)
print(s)
print("Marks of C:",s["C"])
print("Maximum:",s.max())
print("Minimum:",s.min())
print("Average:",s.mean())
print("Students above 75:")
print(s[s>75])
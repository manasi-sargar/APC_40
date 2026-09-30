import numpy as np
marks=np.array([75,82,68,90,85,72,88,95,60,78,70,84,91,65,73,89,76,80,92,69])
average=np.mean(marks)
print("Class average:",average)
print("Above average:",marks[marks>average])
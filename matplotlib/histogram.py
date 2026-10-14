import matplotlib.pyplot as plt
x=[10,20,20,30,30,30,40,40,50,60]
plt.hist(x,bins=5)
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
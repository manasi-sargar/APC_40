import matplotlib.pyplot as plt
x=["Python","Java","C++","HTML"]
y=[40,25,20,15]
plt.pie(y,labels=x,autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()
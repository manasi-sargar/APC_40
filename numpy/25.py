import numpy as np
a=np.random.randint(1,101,size=(3,4,5))
b=a.flatten()
print("Original:\n",a)
print("Greater than 50:",b[b>50])
print("Even numbers:",b[b%2==0])
print("Less than average:",b[b<np.mean(b)])
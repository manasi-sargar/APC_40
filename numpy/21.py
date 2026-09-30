import numpy as np
a=np.random.randint(1,101,size=(2,3,4))
print("Original:\n",a)
a[a>50]=0
print("Modified:\n",a)
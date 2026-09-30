import numpy as np
a=np.arange(1,25).reshape(2,3,4)
print("Sum of all elements:",np.sum(a))
print("Sum of each layer:",np.sum(a,axis=(1,2)))
print("Sum along rows:",np.sum(a,axis=2))
print("Sum along columns:",np.sum(a,axis=1))
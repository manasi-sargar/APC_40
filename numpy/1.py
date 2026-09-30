#1.	Write a Python program using NumPy to create a one-dimensional array containing 10 integers and display the array, its size, data type, and number of dimensions.
import numpy as np
a=np.array([10,20,30,40,50,60,70,80,90,100])
print(a)
print("Size:",a.size)
print("Data type:",a.dtype)
print("Dimensions:",a.ndim)
from array import array
a=array('i',[10,20,30])
b=array('i')
b.frombytes(a.tobytes())
print(b)
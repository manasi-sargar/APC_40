from array import array
a=array('i',[10,20,30])
f=open("data.bin","wb")
a.tofile(f)
f.close()
print("Data written to file")
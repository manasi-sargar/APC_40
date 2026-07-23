a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
c=int(input("enter the value of c: "))
if a>b and a>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
else:
    print("c is largest")

if a<b and a<c:
    print("a is smallest")
elif b<a and b<c:
    print("b is smallest")
else:
    print("c is smallest")

#4.	Create a function simple_interest(p, r, t) to calculate simple interest.
def simple_interest(p, r, t):
    return (p * r * t) / 100
p=float(input("principal: "))
r=float(input("rate: "))
t=float(input("time: "))
print("simple interest: ",simple_interest(p, r, t))
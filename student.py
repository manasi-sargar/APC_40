# write a program and evaluate student performance
# if per>=90->excellent performance
# if per>=80->very good performance
# if per>=70->good performance
# if per>=60->average performance
# else poor performance

per=int(input("enter percentage: "))
if per>=90:
    print(("excellent performance"))
elif per>=80:
    print(("very good performance"))
elif per>=70:
    print((" good performance"))
elif per>=60:
    print(("average performance"))
else:
    print(("poor performance"))

def calculate(marks):
    total = sum(marks)
    percentage = total / 5
    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "F"
    return total, percentage, grade
students = []
for i in range(3):
    name = input("Name: ")
    roll = int(input("Roll No: "))
    marks = []
    for j in range(5):
        marks.append(float(input("Marks: ")))
    total, percentage, grade = calculate(marks)
    students.append([name, roll, total, percentage, grade])
for student in students:
    print(student)
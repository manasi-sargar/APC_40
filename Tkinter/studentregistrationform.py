
import tkinter as tk
from tkinter import messagebox
def register():
    name=name_entry.get().strip()
    roll=roll_entry.get().strip()
    course=course_entry.get().strip()
    gender=gender_var.get()
    if name=="" or roll=="" or course=="" or gender=="":
        messagebox.showerror("Error","All fields are required")
    elif not name.replace(" ","").isalpha():
        messagebox.showerror("Error","Name must contain only letters")
    elif not roll.isdigit():
        messagebox.showerror("Error","Roll number must contain only digits")
    else:
        messagebox.showinfo("Success","Registration Successful!")
root=tk.Tk()
root.title("Student Registration Form")
root.geometry("350x350")
tk.Label(root,text="Student Registration Form",font=("Arial",16,"bold")).pack(pady=10)
tk.Label(root,text="Student Name").pack()
name_entry=tk.Entry(root)
name_entry.pack()
tk.Label(root,text="Roll Number").pack()
roll_entry=tk.Entry(root)
roll_entry.pack()
tk.Label(root,text="Course").pack()
course_entry=tk.Entry(root)
course_entry.pack()
tk.Label(root,text="Gender").pack()
gender_var=tk.StringVar()
tk.Radiobutton(root,text="Male",variable=gender_var,value="Male").pack()
tk.Radiobutton(root,text="Female",variable=gender_var,value="Female").pack()
tk.Button(root,text="Register",command=register).pack(pady=15)
root.mainloop()

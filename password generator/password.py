from tkinter import *
import random
import string


def password_generator():
    length = int(length_entry.get())
    char = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(char)
    for i in range(length))
    password_variable.set(password)

root =Tk()
root.geometry("400x600")
root.title("Password generator")

f1 =Frame(root,borderwidth=7,relief=SUNKEN,bg="orange")
f1.pack(side=TOP,fill="x")

length_lable = Label(f1,text="Password Generator",font="Arial 25 bold",fg="blue")
length_lable.pack(pady=20)

length_entry = Entry(root)
length_entry.pack(pady=20)

submit_button = Button(root,text="Generate Password",command=password_generator,font="Arial 18 bold",fg="green")
submit_button.pack(pady=50)


password_here = Label(root,text="Your Password is Here 🥰",font="Arial 15 bold")
password_here.pack(pady=10)
password_variable = StringVar()
pass_lable = Label(root,textvariable=  password_variable,font="Arial 15 bold",fg="red")
pass_lable.pack(pady=50)

root.mainloop()
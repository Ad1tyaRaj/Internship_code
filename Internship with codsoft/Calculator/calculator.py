from tkinter import *


def click(event):
    text = event.widget.cget("text")
    # print(text)
    if text == "=":
        if Screen.get().isdigit():
            value = int(Screen.get())
        else:
            try:

                value = eval(Screen.get())

            except Exception as e:
                print(e)
                value ="Erorr"

        Screen.set(value)
        cal_screen.update()



    elif text == "C":
        Screen.set("")
        cal_screen.update()

    else:
        Screen.set(Screen.get()+text)
        cal_screen.update()




root = Tk()
root.title("calculator")
root.geometry("400x600")
root.config(background="orange")
root.wm_iconbitmap("1calculator.ico")

Screen = StringVar()
Screen.set("")

cal_screen = Entry(root,textvariable=Screen,font="Arial 18 bold")
cal_screen.pack(pady=20,ipadx=25,ipady=5)


mainframe = Frame(root,bg="red")

# frist Botton
frame = Frame(mainframe,bg="red")
Button1 = Button(frame,text="7",font="Arial 18 bold")
Button1.pack(padx=10,pady=10,ipadx=10,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)

Button1 = Button(frame,text="8",font="Arial 18 bold")
Button1.pack(padx=10,pady=10,ipadx=10,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)

Button1 = Button(frame,text="9",font="Arial 18 bold")
Button1.pack(padx=10,pady=10,ipadx=10,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)

Button1 = Button(frame,text="0",font="Arial 18 bold")
Button1.pack(padx=11,pady=10,ipadx=12,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)
frame.pack()


# second button

frame = Frame(mainframe,bg="red")
Button1 = Button(frame,text="4",font="Arial 18 bold")
Button1.pack(padx=10,pady=10,ipadx=10,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)

Button1 = Button(frame,text="5",font="Arial 18 bold")
Button1.pack(padx=10,pady=10,ipadx=10,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)

Button1 = Button(frame,text="6",font="Arial 18 bold")
Button1.pack(padx=10,pady=10,ipadx=10,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)

Button1 = Button(frame,text="+",font="Arial 18 bold")
Button1.pack(padx=11,pady=10,ipadx=12,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)
frame.pack()


# third button

frame = Frame(mainframe,bg="red")
Button1 = Button(frame,text="1",font="Arial 18 bold")
Button1.pack(padx=10,pady=10,ipadx=10,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)

Button1 = Button(frame,text="2",font="Arial 18 bold")
Button1.pack(padx=10,pady=10,ipadx=10,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)

Button1 = Button(frame,text="3",font="Arial 18 bold")
Button1.pack(padx=10,pady=10,ipadx=10,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)

Button1 = Button(frame,text="-",font="Arial 18 bold")
Button1.pack(padx=11,pady=10,ipadx=12,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)
frame.pack()

# operator buttons

frame = Frame(mainframe,bg="red")
Button1 = Button(frame,text="=",font="Arial 18 bold")
Button1.pack(padx=11,pady=10,ipadx=12,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)

Button1 = Button(frame,text=".",font="Arial 18 bold")
Button1.pack(padx=11,pady=10,ipadx=12,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)

Button1 = Button(frame,text="/",font="Arial 18 bold")
Button1.pack(padx=11,pady=10,ipadx=11,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)

Button1 = Button(frame,text="*",font="Arial 18 bold")
Button1.pack(padx=11,pady=10,ipadx=12,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)
frame.pack()

# new add button

frame = Frame(mainframe,bg="red")
Button1 = Button(frame,text="C",font="Arial 18 bold")
Button1.pack(padx=11,pady=10,ipadx=12,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)

Button1 = Button(frame,text="Codsoft_Adi",font="Arial 18 bold")
Button1.pack(padx=11,pady=25,ipadx=12,ipady=10,side=LEFT)
Button1.bind("<Button-1>",click)


frame.pack(side=LEFT)

mainframe.pack(pady=20)

root.mainloop()
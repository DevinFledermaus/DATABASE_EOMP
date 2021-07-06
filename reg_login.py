from tkinter import *
from tkinter import messagebox
import mysql.connector


root = Tk()
root.geometry("700x500")
root.resizable(False, False)
root.title("Register Login at LifeChoices")
root.config(bg="blue")


def register():
    root.destroy()
    import sign_out


def clear():
    ent1.delete(0, END)
    ent2.delete(0, END)


def exit_btn():
    msg_box = messagebox.askquestion("Heading Out?", "Are you sure you want to leave this program?")
    if msg_box == "yes":
        root.destroy()


# LABELS
lbl1 = Label(root, text="Please enter Username:", bg="blue", font=('Arial', 15))
lbl1.place(x=50, y=100)
lbl2 = Label(root, text="Please enter Password:", bg="blue", font=('Arial', 15))
lbl2.place(x=350, y=100)


# Entries
ent1 = Entry(root, width=30)
ent1.place(x=50, y=150)
ent2 = Entry(root, width=30, show="*")
ent2.place(x=350, y=150)

# Buttons
btn = Button(root, text="Register Login", width=10, bg="green", command=register, borderwidth=5)
btn.place(x=120, y=250)
clrbtn = Button(root, text="Clear", width=10, bg="yellow", command=clear, borderwidth=5)
clrbtn.place(x=410, y=250)
extbtn = Button(root, text="Exit", width=10, bg="red", command=exit_btn, borderwidth=5)
extbtn.place(x=270, y=350)


# Run mainloop
root.mainloop()

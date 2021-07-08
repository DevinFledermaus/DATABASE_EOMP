from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("700x500")
root.resizable(False, False)
root.title("LifeChoices Online")
root.config(bg="blue")


def login():
    root.destroy()
    import Login


def register():
    root.destroy()
    import Register


def admin():
    root.destroy()
    import Admin_login


# Image
img = PhotoImage(file="images.png")
Label(root, image=img).place(x=230, y=10)

# Buttons
btn = Button(root, text="Login", width=10, bg="white", command=login, borderwidth=5)
btn.place(x=190, y=300)
btn2 = Button(root, text="Register", width=10, bg="white", command=register, borderwidth=5)
btn2.place(x=380, y=300)
btn3 = Button(root, text="Admin", width=12, bg="black", fg="white", command=admin, borderwidth=5)
btn3.place(x=278, y=380)


root.mainloop()

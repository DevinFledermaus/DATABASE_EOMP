from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("700x500")
root.resizable(False, False)
root.title("LifeChoices Online")
root.config(bg="blue")


def logout():
    root.destroy()
    import main


# Image
img = PhotoImage(file="images.png")
Label(root, image=img).place(x=235, y=10)

# Buttons
btn = Button(root, text="Logout", width=10, bg="blue", command=logout, borderwidth=5)
btn.place(x=290, y=300)


root.mainloop()

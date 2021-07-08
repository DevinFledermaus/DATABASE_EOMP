from tkinter import *
from tkinter import messagebox
import mysql.connector


root = Tk()
root.geometry("700x500")
root.resizable(False, False)
root.title("Login as Admin")
root.config(bg="blue")


def enter():
    name = ent1.get()
    surname = ent2.get()
    if name == "" or surname == "":
        messagebox.showerror("ERROR!!", "Please Enter Name AND Surname")
    elif not name.isalpha() or surname.isalpha():
        messagebox.showerror("ERROR!!", "Please Enter Name and Surname Correctly")
    else:
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoices_Online', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

        sql = "INSERT INTO Login( Name, Surname, Id_number, Phone_number) \n VALUES( %s, %s, %s, %s)"
        val = ("Nuts", "Deez", "5746981230123", "0741258954")
        exec = mycursor.execute(sql, val)

        mydb.commit()
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
lbl1 = Label(root, text="Please enter Your Name:", bg="blue", font=('Arial', 15))
lbl1.place(x=50, y=100)
lbl2 = Label(root, text="Please enter Your Surname:", bg="blue", font=('Arial', 15))
lbl2.place(x=350, y=100)


# Entries
ent1 = Entry(root, width=30)
ent1.place(x=50, y=150)
ent2 = Entry(root, width=30)
ent2.place(x=350, y=150)

# Buttons
btn = Button(root, text="Login", width=10, bg="green", command=enter, borderwidth=5)
btn.place(x=120, y=250)
clrbtn = Button(root, text="Clear", width=10, bg="yellow", command=clear, borderwidth=5)
clrbtn.place(x=410, y=250)
extbtn = Button(root, text="Exit", width=10, bg="red", command=exit_btn, borderwidth=5)
extbtn.place(x=270, y=350)


# Run mainloop
root.mainloop()

from tkinter import *
from tkinter import messagebox
import mysql.connector


root = Tk()
root.geometry("700x500")
root.resizable(False, False)
root.title("Register at LifeChoices")
root.config(bg="blue")


def register():
    # Kin details
    kin_name = ent1.get()
    kin_surname = ent2.get()
    kin_phone_number = ent3.get()
    if kin_name == "" or kin_surname == "" or kin_phone_number == "":
        messagebox.showerror("ERROR", "Please complete all your details")
    else:
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoices_Online', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

        sql = "INSERT INTO Kin( Name, Surname, Phone_number) \n VALUES( %s, %s, %s)"
        val = (kin_name, kin_surname, kin_phone_number)
        exec = mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        mycursor.execute('Select * from Kin')
        messagebox.showinfo("SUCCESS", "New User's Kin Added")

        root.destroy()
        import sign_out


def clear():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)


def exit_btn():
    msg_box = messagebox.askquestion("Heading Out?", "Are you sure you want to leave this program?")
    if msg_box == "yes":
        root.destroy()


# LABELS
# KIN
headlbl = Label(root, text="Next of Kin Details", bg="blue", font=('Arial', 20))
headlbl.place(x=235, y=10)
lbl1 = Label(root, text="Please enter Kin's First Name:", bg="blue", font=('Arial', 15))
lbl1.place(x=210, y=50)
lbl2 = Label(root, text="Please enter Kin's Last Name:", bg="blue", font=('Arial', 15))
lbl2.place(x=210, y=130)
lbl3 = Label(root, text="Please enter Kin's Phone Number:", bg="blue", font=('Arial', 15))
lbl3.place(x=210, y=210)


# Entries
# KIN
ent1 = Entry(root, width=30)
ent1.place(x=230, y=90)
ent2 = Entry(root, width=30)
ent2.place(x=230, y=170)
ent3 = Entry(root, width=30)
ent3.place(x=230, y=250)


# Buttons
btn = Button(root, text="Register", width=10, bg="green", command=register, borderwidth=5)
btn.place(x=290, y=310)
clrbtn = Button(root, text="Clear", width=10, bg="blue", command=clear, borderwidth=5)
clrbtn.place(x=100, y=400)
extbtn = Button(root, text="Exit", width=10, bg="blue", command=exit_btn, borderwidth=5)
extbtn.place(x=500, y=400)


# Run mainloop
root.mainloop()

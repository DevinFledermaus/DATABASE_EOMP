from tkinter import *
from tkinter import messagebox
import mysql.connector


root = Tk()
root.geometry("700x500")
root.resizable(False, False)
root.title("Login at LifeChoices")
root.config(bg="blue")

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoices_Online', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


def verify():
    query = 'Select *  FROM  Login'
    mycursor.execute(query)
    valid = False
    for x in mycursor:
        if x[1] == ent1.get() and x[3] == ent2.get():
            valid = True
            que = 'INSERT INTO Log() \n VALUES();'
            mycursor.execute(que)
    if not valid:
        messagebox.showerror("ERROR", "User does not exist")
    elif valid:
        messagebox.showinfo("Access Granted", "You have successfully logged in")


def enter():
    name = ent1.get()
    surname = ent2.get()
    if name == "" or surname == "":
        messagebox.showerror("ERROR!!", "Please Enter Name AND Surname")
    else:
        # mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoices_Online', auth_plugin='mysql_native_password')
        #
        # mycursor = mydb.cursor()

        data = "Select * from Login"
        base = mycursor.execute(data)
        login_id = 0
        for x in mycursor:
            login_id = x[0]

        sql = "INSERT INTO Log( Name, Surname, UserID) \n VALUES( %s, %s, %s)"
        val = (name, surname, login_id)
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

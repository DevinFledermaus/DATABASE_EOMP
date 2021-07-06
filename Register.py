from tkinter import *
from tkinter import messagebox
import mysql.connector


root = Tk()
root.geometry("700x500")
root.resizable(False, False)
root.title("Register at LifeChoices")
root.config(bg="blue")

#
# def check_table():
#     mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Hospitals', auth_plugin='mysql_native_password')
#     mycursor = mydb.cursor()
#     xy = mycursor.execute('Select * from Login')
#     for i in mycursor:
#         print(i)
#
#
# def enter(username):
#     mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Hospitals', auth_plugin='mysql_native_password')
#
#     results = []
#     query = 'SELECT * FROM Login WHERE user="' + username + '";'
#     my_cursor = mydb.cursor()
#     my_cursor.execute(query)
#
#     for i in my_cursor:
#         results.append(list(i))
#
#         return results
#
#
def register():
    root.destroy()
    import reg_login
#     user = ent1.get()
#     password = ent2.get()
#     if ent1 == "" or ent2 == "":
#         messagebox.showerror("ERROR", "Please fill in username and password")
#     elif user.isdigit():
#         messagebox.showerror("Error", "Name does not contain letters")
#     else:
#         mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Hospitals', auth_plugin='mysql_native_password')
#
#         mycursor = mydb.cursor()
#
#         sql = "INSERT INTO Login  VALUES (%s, %s)"
#         val = (ent1.get(), ent2.get())
#         mycursor.execute(sql, val)
#
#         mydb.commit()
#
#         print(mycursor.rowcount, "record inserted.")
#         mycursor.execute('Select * from Login')
#         messagebox.showinfo("SUCCESS", "New user and password added")
#

def clear():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)


def exit_btn():
    msg_box = messagebox.askquestion("Heading Out?", "Are you sure you want to leave this program?")
    if msg_box == "yes":
        root.destroy()


# LABELS
# USER
headlbl = Label(root, text="User Details", bg="blue", font=('Arial', 20))
headlbl.place(x=20, y=10)
lbl1 = Label(root, text="Please enter First Name:", bg="blue", font=('Arial', 15))
lbl1.place(x=20, y=50)
lbl2 = Label(root, text="Please enter Last Name:", bg="blue", font=('Arial', 15))
lbl2.place(x=20, y=130)
lbl3 = Label(root, text="Please enter ID Number:", bg="blue", font=('Arial', 15))
lbl3.place(x=20, y=210)
lbl4 = Label(root, text="Please enter Phone Number", bg="blue", font=('Arial', 15))
lbl4.place(x=20, y=290)
# KIN
headlbl2 = Label(root, text="Next of Kin Details", bg="blue", font=('Arial', 20))
headlbl2.place(x=350, y=10)
lbl5 = Label(root, text="Please enter Kin's First Name:", bg="blue", font=('Arial', 15))
lbl5.place(x=350, y=50)
lbl6 = Label(root, text="Please enter Kin's Last Name:", bg="blue", font=('Arial', 15))
lbl6.place(x=350, y=130)
lbl7 = Label(root, text="Please enter Kin's Phone Number:", bg="blue", font=('Arial', 15))
lbl7.place(x=350, y=210)


# Entries
# USER
ent1 = Entry(root, width=30)
ent1.place(x=20, y=90)
ent2 = Entry(root, width=30)
ent2.place(x=20, y=170)
ent3 = Entry(root, width=30)
ent3.place(x=20, y=250)
ent4 = Entry(root, width=30)
ent4.place(x=20, y=330)
# KIN
ent5 = Entry(root, width=30)
ent5.place(x=350, y=90)
ent6 = Entry(root, width=30)
ent6.place(x=350, y=170)
ent7 = Entry(root, width=30)
ent7.place(x=350, y=250)


# Buttons
btn2 = Button(root, text="Register", width=10, bg="green", command=register, borderwidth=5)
btn2.place(x=350, y=310)
clrbtn = Button(root, text="Clear", width=10, bg="blue", command=clear, borderwidth=5)
clrbtn.place(x=100, y=400)
extbtn = Button(root, text="Exit", width=10, bg="blue", command=exit_btn, borderwidth=5)
extbtn.place(x=500, y=400)


# Run mainloop
root.mainloop()

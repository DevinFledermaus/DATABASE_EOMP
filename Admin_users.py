from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

root = Tk()
root.title('User Database')
root.geometry('700x500')
root.resizable(False, False)
root.config(bg="blue")


def exitbtn():
    msg_box = messagebox.askquestion("Are you sure?", "Head back to the login main page?")
    if msg_box == "yes":
        root.destroy()
        import main


def enter():
    msg_box = messagebox.askquestion("Are you sure?", "Move to the Logs?")
    if msg_box == "yes":
        root.destroy()
        import Admin_log


mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoices_Online', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
xy = mycursor.execute('Select * from Login')

window = ttk.Treeview(root)

# Defining columns
window['columns'] = ('id', 'Name', 'Surname', 'Id_number', 'Phone_number')

# Format columns
window.column('#0', width=0, minwidth=0, stretch=NO)  # Phantom column
window.column('id', anchor=CENTER, width=50)
window.column('Name', anchor=W, width=125)
window.column('Surname', anchor=W, width=125)
window.column('Id_number', anchor=W, width=125)
window.column('Phone_number', anchor=W, width=100)

# Defining column headings
window.heading('#0', text='Labels', anchor=CENTER)  # Phantom Column
window.heading('id', text='ID', anchor=CENTER)
window.heading('Name', text='Name', anchor=CENTER)
window.heading('Surname', text='Surname', anchor=CENTER)
window.heading('Id_number', text='ID NO.', anchor=CENTER)
window.heading('Phone_number', text='Phone NO.', anchor=CENTER)

# Obtain data from database
x = 0
for data in mycursor:
    window.insert(parent='', index='end', iid=x, text="", values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
    x += 1

# Placing treeview table
window.pack(pady=20)

# Buttons
btn = Button(root, text="Admin Log", bg="black", fg="white", width=10, borderwidth=5, command=enter)
btn.place(x=200, y=400)
addbtn = Button(root, text="INSERT", width=10, borderwidth=5)
addbtn.place(x=200, y=300)
dltbtn = Button(root, text="DELETE", width=10, borderwidth=5)
dltbtn.place(x=400, y=300)
extbtn = Button(root, text="Exit", bg="red", width=10, borderwidth=5, command=exitbtn)
extbtn.place(x=400, y=400)


# Run Window
root.mainloop()

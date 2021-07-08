from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()
root.title('LOG')
root.geometry('700x500')
root.resizable(False, False)
root.config(bg="blue")


mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoices_Online', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
xy = mycursor.execute('Select * from Log')

window = ttk.Treeview(root)

# Defining columns
window['columns'] = ('id', 'Name', 'Surname', 'UserID', 'Time_in', 'Time_out')

# Format columns
window.column('#0', width=75, minwidth=25)  # Phantom column
window.column('id', anchor=CENTER, width=50)
window.column('Name', anchor=W, width=100)
window.column('Surname', anchor=W, width=100)
window.column('UserID', anchor=W, width=100)
window.column('Time_in', anchor=W, width=100)
window.column('Time_out', anchor=W, width=100)

# Defining column headings
window.heading('#0', text='Labels', anchor=CENTER)  # Phantom Column
window.heading('id', text='ID', anchor=CENTER)
window.heading('Name', text='Name', anchor=CENTER)
window.heading('Surname', text='Surname', anchor=CENTER)
window.heading('UserID', text='UserID', anchor=CENTER)
window.heading('Time_in', text='Sign in', anchor=CENTER)
window.heading('Time_out', text='Sign out', anchor=CENTER)

# Obtain data from database
x = 0
for data in mycursor:
    window.insert(parent='', index='end', iid=x, text="Member", values=(data[0], data[1], data[2], data[3], data[4], data[5]))
    x += 1

# Placing treeview table
window.pack(pady=20)

# Run Window
root.mainloop()

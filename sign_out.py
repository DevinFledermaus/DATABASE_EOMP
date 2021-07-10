from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
root.geometry("700x500")
root.resizable(False, False)
root.title("LifeChoices Online")
root.config(bg="blue")

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoices_Online', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


def sign_out():
    query = 'Select *  FROM  Login'
    mycursor.execute(query)
    valid = False
    for x in mycursor:
        if x[1] == ent1.get() and x[3] == ent2.get():
            valid = True
            que = 'UPDATE Login SET Time_out = CURRENT_TIMESTAMP WHERE id=%s'
            val = x[3]
            mycursor.execute(que, val)
    if not valid:
        messagebox.showerror("ERROR", "User does not exist")
    elif valid:
        messagebox.showinfo("SUCCESS", "You have successfully logged out")
        logout()


def logout():
    query = 'Select *  FROM  Login'
    mycursor.execute(query)
    for x in mycursor:
        if x[1] == ent1.get() and x[3] == ent2.get():
            que = 'DELETE FROM Log WHERE id=' + str(x[0])
            mycursor.execute(que)
    root.destroy()
    import main


# Image
img = PhotoImage(file="images.png")
Label(root, image=img).place(x=235, y=10)


# LABELS
lbl1 = Label(root, text="Please enter Your Name:", bg="blue", font=('Arial', 15))
lbl1.place(x=50, y=250)
lbl2 = Label(root, text="Please enter Your ID Number:", bg="blue", font=('Arial', 15))
lbl2.place(x=350, y=250)


# Entries
ent1 = Entry(root, width=30)
ent1.place(x=50, y=300)
ent2 = Entry(root, width=30)
ent2.place(x=350, y=300)

# Buttons
btn = Button(root, text="Logout", width=10, bg="blue", command=logout, borderwidth=5)
btn.place(x=290, y=400)


root.mainloop()

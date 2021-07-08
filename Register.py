from tkinter import *
from tkinter import messagebox
import mysql.connector


root = Tk()
root.geometry("700x500")
root.resizable(False, False)
root.title("Register at LifeChoices")
root.config(bg="blue")


def register():
    # User details
    name = ent1.get()
    surname = ent2.get()
    id_no = ent3.get()
    phone_no = ent4.get()
    # Functionality
    if name == "" or surname == "" or id_no == "" or phone_no == "":
        messagebox.showerror("ERROR", "Please complete all your details")
    # elif not name.isalpha() or not surname.isalpha():
    #     messagebox.showerror("ERROR", "Names do not contain letters")
    # elif id_no.isdigits() or phone_no.isdigits():
    #     messagebox.showerror("ERROR", "ID and Phone numbers only contain numbers")
    # elif id_no > 13:
    #     messagebox.showerror("ERROR", "ID number must contain 13 numbers")
    # elif phone_no > 10:
    #     messagebox.showerror("ERROR", "Phone number must contain 10 numbers")
    else:
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoices_Online', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

        sql = "INSERT INTO Login( Name, Surname, Id_number, Phone_number) \n VALUES( %s, %s, %s, %s)"
        val = (name, surname, id_no, phone_no)
        exec = mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        mycursor.execute('Select * from Login')
        messagebox.showinfo("New User Added", "Please enter Next of Kin's details")

        root.destroy()
        import Next_of_kin


def clear():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)

def exit_btn():
    msg_box = messagebox.askquestion("Heading Out?", "Are you sure you want to leave this program?")
    if msg_box == "yes":
        root.destroy()


# LABELS
# USER
headlbl = Label(root, text="User Details", bg="blue", font=('Arial', 30))
headlbl.place(x=250, y=10)
lbl1 = Label(root, text="Please enter First Name:", bg="blue", font=('Arial', 15))
lbl1.place(x=20, y=120)
lbl2 = Label(root, text="Please enter Last Name:", bg="blue", font=('Arial', 15))
lbl2.place(x=20, y=220)
lbl3 = Label(root, text="Please enter ID Number:", bg="blue", font=('Arial', 15))
lbl3.place(x=350, y=120)
lbl4 = Label(root, text="Please enter Phone Number:", bg="blue", font=('Arial', 15))
lbl4.place(x=350, y=220)


# Entries
# USER
ent1 = Entry(root, width=30)
ent1.place(x=20, y=150)
ent2 = Entry(root, width=30)
ent2.place(x=20, y=250)
ent3 = Entry(root, width=30)
ent3.place(x=350, y=150)
ent4 = Entry(root, width=30)
ent4.place(x=350, y=250)


# Buttons
btn2 = Button(root, text="Register", width=10, bg="green", command=register, borderwidth=5)
btn2.place(x=290, y=310)
clrbtn = Button(root, text="Clear", width=10, bg="blue", command=clear, borderwidth=5)
clrbtn.place(x=100, y=400)
extbtn = Button(root, text="Exit", width=10, bg="blue", command=exit_btn, borderwidth=5)
extbtn.place(x=500, y=400)


# Run mainloop
root.mainloop()

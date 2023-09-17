from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)


def connect_database():
    if emailEntry.get() == '' or usernameEntry.get == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
        messagebox.showerror("Error", "All fields are required")
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror("Error", "Password Mismatch")
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Aishu@123')
            myCursor = con.cursor()
        except:
            messagebox.showerror("Error", " Database Connectivity Issue, Please Try Again")
            return
        try:
            query = 'create database VirtualMouse'
            myCursor.execute(query)
            query = 'use VirtualMouse'
            myCursor.execute(query)
            query = "create table userdata(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))"
            myCursor.execute(query)
        except:
            myCursor.execute('use VirtualMouse')

        query = 'select * from userdata where username=%s'
        myCursor.execute(query, (usernameEntry.get()))

        row = myCursor.fetchone()
        if row != None:
            messagebox.showerror("Error", " Username already exists")
        else:
            query = 'insert into userdata(email, username, password) values(%s, %s, %s)'
            myCursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
            signup_window.destroy()
            import SignInPage


def login_page():
    signup_window.destroy()
    import SignInPage


signup_window = Tk()
signup_window.title("SignUp Page")
signup_window.resizable(False, False)

background = ImageTk.PhotoImage(file='bg.jpeg')

bgLabel = Label(signup_window, image=background)
bgLabel.grid()

frame = Frame(signup_window)
frame.place(x=555, y=100)

heading = Label(frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light ', 18, 'bold')
                , bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light ', 10, 'bold')
                   , fg='firebrick1', bg='white')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10.0))

emailEntry = Entry(frame, width=25, font=('Microsoft Yahei UI Light ', 10, 'bold')
                   , fg='white', bg='firebrick1')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

usernameLabel = Label(frame, text='Username', font=('Microsoft Yahei UI Light ', 10, 'bold')
                      , fg='firebrick1', bg='white')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10.0))

usernameEntry = Entry(frame, width=25, font=('Microsoft Yahei UI Light ', 10, 'bold')
                      , fg='white', bg='firebrick1')
usernameEntry.grid(row=4, column=0, sticky='w', padx=25)

passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light ', 10, 'bold')
                      , fg='firebrick1', bg='white')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10.0))

passwordEntry = Entry(frame, width=25, font=('Microsoft Yahei UI Light ', 10, 'bold')
                      , fg='white', bg='firebrick1')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

confirmLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light ', 10, 'bold')
                     , fg='firebrick1', bg='white')
confirmLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10.0))

confirmEntry = Entry(frame, width=25, font=('Microsoft Yahei UI Light ', 10, 'bold')
                     , fg='white', bg='firebrick1')
confirmEntry.grid(row=8, column=0, sticky='w', padx=25)

signupButton = Button(frame, text='Signup', font=('Open Sans', 16, 'bold'),
                      bd=0, bg='firebrick1', fg='white', activebackground='firebrick1',
                      activeforeground='white', width=17, command=connect_database)
signupButton.grid(row=10, column=0, sticky='w', pady=10, padx=25)

alreadyaccount = Label(frame, text="Already have an account?", font=('Open Sans', '9', 'bold'),
                       bg='white', fg='firebrick1')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

loginButton = Button(frame, text='Log in ', font=('Open Sans', 9, 'bold underline')
                     , bg='white', fg='blue', bd=0, cursor='hand2', activebackground='white'
                     , activeforeground='blue', command=login_page)
loginButton.place(x=210, y=374)

signup_window.mainloop()

from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', ' All Fields Are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Aishu@123')
            myCursor = con.cursor()
        except:
            messagebox.showerror("Error", ' Connection is not established try again')
            return
        query = 'use VirtualMouse'
        myCursor.execute(query)
        query = 'select * from userdata where username=%s and password=%s'
        myCursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = myCursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid username and Password')
        else:
            messagebox.showinfo('Welcome', 'Login is Successful')
            login_window.destroy()
            import VirtualMouse


def signup_page():
    login_window.destroy()
    import SignUpPage


def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get() == 'UserName':
        usernameEntry.delete(0, END)


def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


# GUI Part
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0, 0)
login_window.title('Login Page')

bgImage = ImageTk.PhotoImage(file='bg.jpeg')

bgLable = Label(login_window, image=bgImage)
bgLable.pack()
heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light  '
                                                       , 23, 'bold'),
                bg='white', fg='firebrick1')
heading.place(x=605, y=120)

usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light ', 11, 'bold'), bg='white', bd=0,
                      fg='firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'UserName')

usernameEntry.bind('<FocusIn>', user_enter)

frame1 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame1.place(x=580, y=222)

passwordEntry = Entry(login_window, width=25,
                      font=('Microsoft Yahei UI Light ', 11, 'bold'),
                      bd=0, fg='firebrick1')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', password_enter)

frame2 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame2.place(x=580, y=282)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',
                   command=hide)
eyeButton.place(x=800, y=255)

loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1',
                     activeforeground='white', activebackground='firebrick1',
                     cursor='hand2', bd=0, width=19, command=login_user)
loginButton.place(x=578, y=350)

signupLabel = Label(login_window, text='Dont have an account?', font=('Open Sans', 9, 'bold'), fg='firebrick1',
                    bg='white')
signupLabel.place(x=583, y=450)

newaccountButton = Button(login_window, text='Create new Account', font=('Open Sans', 9, 'bold underline'), fg='blue',
                          bg='white', activeforeground='blue', activebackground='firebrick1',
                          cursor='hand2', bd=0, command=signup_page)
newaccountButton.place(x=727, y=450)

login_window.mainloop()

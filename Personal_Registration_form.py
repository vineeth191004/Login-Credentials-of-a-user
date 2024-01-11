from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql
import re
import hashlib

# window size
registration = Tk()
registration.title("Personal Registration Form")
registration.geometry('540x820+200+10')

def bck():
    registration.destroy()
    import Login_screen



registration.resizable(0,0)

# database section
def submit():
    if firstnameEntry.get() == '':
        messagebox.showerror('Alert!', 'Please Enter your First name')

    elif lastnameEntry.get() == '':
        messagebox.showerror('Alert!', 'Please Enter your Last name')

    elif emailEntry.get() == '':
        messagebox.showerror('Alert!', 'Please Enter your Email')

    elif gender.get() == '':
        messagebox.showerror('Alert!', 'Please select your gender')

    elif OM.get() == '':
        messagebox.showerror('Alert!', 'Please select your country')

    elif usernameEntry.get() == '':
        messagebox.showerror('Alert!', 'Please enter your username')

    elif passwordEntry.get() == '':
        messagebox.showerror('Alert!', 'Please enter your password')

    elif ConfirmpasswordEntry.get() == '':
        messagebox.showerror('Alert!', 'Please confirm your password')

    elif passwordEntry.get() != ConfirmpasswordEntry.get():
        messagebox.showerror('Alert!', 'Password do not match')

    elif not re.match("^[A-Za-z]+$", firstnameEntry.get()):
        messagebox.showerror('Alert!', 'Please enter a valid First Name')

    elif not re.match("^[A-Za-z]+$", lastnameEntry.get()):
        messagebox.showerror('Alert!', 'Please enter a valid Last Name')

    elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', emailEntry.get()):
        messagebox.showerror('Alert!', 'Please enter a valid Email')


    elif (len(usernameEntry.get()) < 5 or len(usernameEntry.get()) > 20):
        messagebox.showerror('Alert!', 'Username should be between 5 and 20 characters')

    elif (len(passwordEntry.get()) < 8 or len(passwordEntry.get()) > 20):
        messagebox.showerror('Alert!', 'Password should be between 8 and 20 characters')

    elif not re.match("^[a-zA-Z0-9_]+$", usernameEntry.get()):
        messagebox.showerror('Alert!', 'Username should only contain letters, numbers, and underscores')

    elif not check_password_strength(passwordEntry.get()):
        messagebox.showerror('Alert!', 'Password should be at least 8 characters long and contain at least one digit, one uppercase letter, and one lowercase letter')

    else:
            salt = '5gz'
            password_1 = passwordEntry.get() + salt
            confirm_password_2 = ConfirmpasswordEntry.get() + salt
            password_hash = hashlib.md5(password_1.encode()).hexdigest()
            confirm_password_hash = hashlib.md5(confirm_password_2.encode()).hexdigest()
            db=pymysql.connect(host='localhost', user='root', password='Vineeth04!',database='Personal_registration_form')
            cur=db.cursor()

            try:
                query = 'create database Personal_registration_form'
                cur.execute(query)
                query = 'Use Personal_registration_form'
                cur.execute(query)
                # messagebox.showinfo('success', 'successful connection')
                # print('worked')

                # query = 'DROP TABLE P_DETAILS'
                # cur.execute(query)


                query = ''' CREATE TABLE P_DETAILS(
            		                        ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                                            FIRSTNAME VARCHAR(40),
                                            LASTNAME VARCHAR(40),
                                            EMAIL VARCHAR(40),
                                            SCHOOL VARCHAR(40),
                                            UNIVERSITY VARCHAR(40),
                                            GENDER VARCHAR(7),
                                            COUNTRY VARCHAR(40),
                                            USERNAME VARCHAR(40),
                                            PASSWORD VARCHAR(40),
                                            CONFIRMPASSWORD VARCHAR(40)
                                            );'''
                cur.execute(query)
                messagebox.showinfo('Success', 'fields created successfully')

            except:
                cur.execute('use Personal_registration_form')
                query = '''INSERT INTO P_DETAILS(FIRSTNAME,LASTNAME,EMAIL,SCHOOL,UNIVERSITY,GENDER,
                                            COUNTRY,USERNAME,PASSWORD,CONFIRMPASSWORD) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                cur.execute(query, (firstnameEntry.get(), lastnameEntry.get(), emailEntry.get(), schoolnameEntry.get(),
                                    UniversitynameEntry.get(), gender.get(),
                                    OM.get(), usernameEntry.get(), password_hash, confirm_password_hash))
                db.commit()
                db.close()
                messagebox.showinfo('Success', 'Successful Registration')

                firstnameEntry.delete(0, END)
                lastnameEntry.delete(0, END)
                emailEntry.delete(0, END)
                schoolnameEntry.delete(0, END)
                UniversitynameEntry.delete(0, END)
                gender.set(0)
                OM.set(0)
                usernameEntry.delete(0, END)
                passwordEntry.delete(0, END)
                ConfirmpasswordEntry.delete(0, END)



def show1():
    passwordEntry.config(show='#')
    check1.config(command=hide1)


def hide1():
    passwordEntry.config(show='')
    check1.config(command=show1)


def show2():
    ConfirmpasswordEntry.config(show='#')
    check2.config(command=hide2)


def hide2():
    ConfirmpasswordEntry.config(show='')
    check2.config(command=show2)

def check_password_strength(password):
    if len(password) < 8 or len(password) > 20:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True






# section for getting data from the entry fields
firstname = StringVar()
lastname = StringVar()
email = StringVar()
schoolname = StringVar()
Universityname = StringVar()
gender = StringVar()
OM = StringVar()
username = StringVar()
password = StringVar()
Confirmpassword = StringVar()


# frame
OM = StringVar()
frame = Frame(registration, width=1000, height=1400, bg='black', bd=8)
frame.place(x=0, y=0)
country = ['Algeria', 'Australia', 'Austria', 'Egypt', 'India', 'Sri lanka']
OM.set('Select Country')

# labels and entry fields
heading = Label(frame, text='Personal Registration Form', fg='Red', bg='Black', font=('Calibre', 24, 'bold'))
heading.place(x=50, y=3)

firstnamelbl = Label(frame, text='First Name:', fg='Blue', bg='Black', font=('Calibre', 20, 'bold'))
firstnamelbl.place(x=10, y=110)

firstnameEntry = Entry(frame, width=30, borderwidth=2)
firstnameEntry.place(x=310, y=120)

lasttnamelbl = Label(frame, text='Last Name:', fg='Blue', bg='Black', font=('Calibre', 20, 'bold'))
lasttnamelbl.place(x=10, y=170)

lastnameEntry = Entry(frame, width=30, borderwidth=2)
lastnameEntry.place(x=310, y=180)

emaillbl = Label(frame, text='Email:', fg='Blue', bg='Black', font=('Calibre', 20, 'bold'))
emaillbl.place(x=10, y=230)

emailEntry = Entry(frame, width=30, borderwidth=2)
emailEntry.place(x=310, y=240)

schoolnamelbl = Label(frame,text='School name :', fg='Blue', bg='Black', font=('Calibre',20,'bold'))
schoolnamelbl.place(x=10,y=290)

schoolnameEntry = Entry(frame,width=30,borderwidth=2)
schoolnameEntry.place(x=310,y=300)

Universitynamelbl = Label(frame,text='University name :', fg='Blue', bg='Black', font=('Calibre',20,'bold'))
Universitynamelbl.place(x=10,y=350)

UniversitynameEntry = Entry(frame,width=30,borderwidth=2)
UniversitynameEntry.place(x=310,y=360)


genderlbl = Label(frame, text='Select Gender:', fg='Blue', bg='Black', font=('Calibre', 20, 'bold'))
genderlbl.place(x=10, y=420)

gender.set(0)
genderRadio1 = Radiobutton(frame, text='Male', variable=gender, value='Male', font='Tahoma 13 bold')
genderRadio1.place(x=310, y=420)

genderRadio2 = Radiobutton(frame, text='Female', variable=gender, value='Female', font='Tahoma 13 bold')
genderRadio2.place(x=430, y=420)

countryLabelDropdown = Label(frame, text='Select Country:', fg='Blue', bg='Black', font=('Calibre', 20, 'bold'))
countryLabelDropdown.place(x=10, y=480)

countryLabelDropdown = OptionMenu(frame, OM, *country)
countryLabelDropdown.place(x=310, y=480)

countryLabelDropdown.config(width=18, font=('Calibre', 13, 'bold'), fg='black')

usernamelbl = Label(frame, text='Username:', fg='Blue', bg='Black', font=('Calibre', 20, 'bold'))
usernamelbl.place(x=10, y=530)

usernameEntry = Entry(frame, width=30, borderwidth=2)
usernameEntry.place(x=310, y=540)

passwordlbl = Label(frame, text='Password:', fg='Blue', bg='Black', font=('Calibre', 20, 'bold'))
passwordlbl.place(x=10, y=590)

passwordEntry = Entry(frame, width=30, borderwidth=2)
passwordEntry.place(x=310, y=600)

Confirmpasswordlbl = Label(frame, text='Confirm Password:', fg='Blue', bg='Black', font=('Calibre', 20, 'bold'))
Confirmpasswordlbl.place(x=10, y=650)

ConfirmpasswordEntry = Entry(frame, width=30, borderwidth=2)
ConfirmpasswordEntry.place(x=310, y=660)

submitbtn = Button(frame, text='SUBMIT', width=16, borderwidth=5, height=2, bg='Violet', border=2,
                   font=('Calibre', 15, 'bold'), command=submit)
submitbtn.place(x=155, y=730)

bckbtn = Button(frame, text='<<', width=15, borderwidth=2, height=2, bg='black', fg='white', cursor='hand2',command=bck)
bckbtn.place(x=2, y=750)

# check buttons
check1 = Checkbutton(frame, text='', bg='black', command=show1)
check1.place(x=500, y=600)

check2 = Checkbutton(frame, text='', bg='black', command=show2)
check2.place(x=500, y=660)

registration.mainloop()


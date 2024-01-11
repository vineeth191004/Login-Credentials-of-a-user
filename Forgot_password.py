from tkinter import *
from tkinter import messagebox, simpledialog
import pymysql
import hashlib


#windows
windows = Tk()
windows.geometry('500x460+500+10')
windows.resizable(0,0)
windows.title("Forgot Password")

#frame
frame=Frame(windows, width=540, height=640, bg='black', bd=8)
frame.place(x=0, y=0)

Font = ("Calibre",18,'bold')

def back():
    windows.destroy()
    import Login_screen

def submit():
    if emailEntry.get() == '' or newpasswordEntry.get() == ''or confirmpasswordEntry.get() == '':
        messagebox.showerror('Alert!','Entry fields must be enetered')
        return
    elif newpasswordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Alert!','Passwords donot match')
        return
    else:
        salt = '5gz'
        password_2 = newpasswordEntry.get() + salt
        confirm_password_1 = confirmpasswordEntry.get() + salt
        new_password_hash = hashlib.md5(password_2.encode()).hexdigest()
        new_confirm_password_hash = hashlib.md5(confirm_password_1.encode()).hexdigest()
        db = pymysql.connect(host='localhost', user='root', password='Vineeth04!',
                             database='Personal_registration_form')
        cur = db.cursor() #is to help us execute our query

        query = 'select * from p_details where email=%s'
        cur.execute(query,(emailEntry.get()))

        row = cur.fetchone()
        print(row)# to fetch for existing data
        if row == None:
            messagebox.showerror('Alert', 'This email doesnot exist. Please input your registered email')
            return
        else:

            schoolname = simpledialog.askstring('Additional Details', 'What is your school name?')
            if schoolname is None: # user clicked cancel or x
                return
            if schoolname != row[4]:
                messagebox.showerror('Alert!','School name does not match with registered one')
                return schoolname

            Universityname = simpledialog.askstring('Additional Details', 'What is your University name?')
            if Universityname is None:
                return
            if Universityname != row[5]:
                messagebox.showerror('Alert!','University name does not match with registered one')
                return schoolname

            query='update p_details set password=%s where email=%s' #this is the line of code to update the password
            cur.execute(query,(new_password_hash,emailEntry.get()))
            query='update p_details set confirmpassword=%s where email=%s'
            cur.execute(query,(new_confirm_password_hash,emailEntry.get()))
            db.commit()
            db.close()
            messagebox.showinfo('Success', 'Successful changes. Please login with new password')




            emailEntry.delete(0,END)
            newpasswordEntry.delete(0, END)
            confirmpasswordEntry.delete(0,END)


            windows.destroy()
            import Login_screen









#Labels and btns
heading = Label(frame, text='FORGOT PASSWORD', fg='Blue', bg='black', font=('Calibre',25,'bold'))
heading.place(x=80, y=3)

passwordImage = PhotoImage(file='lock (1).png')
passwordLabel = Label(frame,image=passwordImage)
passwordLabel.place(x=25,y=3)


emailLbl = Label(frame, text='Email : ',fg='sky blue', bg='black',font=Font)
emailLbl.place(x=3,y=110)

emailEntry = Entry(frame, width=30, borderwidth=2)
emailEntry.place(x=250,y=115)


newpasswordLbl = Label(frame, text='New Password : ',fg='sky blue', bg='black',font=Font)
newpasswordLbl.place(x=3,y=190)

newpasswordEntry = Entry(frame, width=30, borderwidth=2)
newpasswordEntry.place(x=250,y=195)


confirmpasswordLbl = Label(frame, text='Confirm Password : ',fg='sky blue', bg='black',font=Font)
confirmpasswordLbl.place(x=3,y=270)

confirmpasswordEntry = Entry(frame, width=30, borderwidth=2)
confirmpasswordEntry.place(x=250,y=275)

bckbtn = Button(frame, text="<<", width=7, borderwidth=5, height=2, bg='black', fg='white', cursor='hand2',border=2, command=back)
bckbtn.place(x=10, y=400)

submitbtn = Button(frame,text='Submit', width=15, height=2, bg='violet', fg='white', cursor='hand2', border=2, borderwidth=5, font=Font,command=submit)
submitbtn.place(x=130, y=350)










windows.mainloop()
from tkinter import *
from tkinter import messagebox, simpledialog
import pymysql



#windows
windows = Tk()
windows.geometry('500x460+500+10')
windows.resizable(0,0)
windows.title("Forgot Username")

#frame
frame=Frame(windows, width=540, height=640, bg='black', bd=8)
frame.place(x=0, y=0)

Font = ("Calibre",18,'bold')

def back():
    windows.destroy()
    import Login_screen

def submit():
    if usernameEntry.get() == '' or emailEntry.get() == '':
        messagebox.showerror('Alert!','Entry fields must be enetered')
        return
    else:
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

            query='update p_details set username=%s where email=%s' #this is the line of code to update the password
            cur.execute(query,(usernameEntry.get(),emailEntry.get()))
            db.commit()
            db.close()
            messagebox.showinfo('Success', 'Successful changes. Please login with new password')




            usernameEntry.delete(0,END)
            emailEntry.delete(0,END)


            windows.destroy()
            import Login_screen









#Labels and btns
heading = Label(frame, text='FORGOT USERNAME', fg='Blue', bg='black', font=('Calibre',25,'bold'))
heading.place(x=80, y=3)

usernameLbl = Label(frame, text='Username : ',fg='sky blue', bg='black',font=Font)
usernameLbl.place(x=3,y=120)

usernameEntry = Entry(frame, width=30, borderwidth=2)
usernameEntry.place(x=250,y=125)


emailLbl = Label(frame, text='Email : ',fg='sky blue', bg='black',font=Font)
emailLbl.place(x=3,y=170)

emailEntry = Entry(frame, width=30, borderwidth=2)
emailEntry.place(x=250,y=175)


bckbtn = Button(frame, text="<<", width=7, borderwidth=5, height=2, bg='black', fg='white', cursor='hand2',border=2, command=back)
bckbtn.place(x=10, y=400)

submitbtn = Button(frame,text='Submit', width=15, height=2, bg='violet', fg='white', cursor='hand2', border=2, borderwidth=5, font=Font,command=submit)
submitbtn.place(x=130, y=350)










windows.mainloop()
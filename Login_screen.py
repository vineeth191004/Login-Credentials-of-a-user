from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, simpledialog
import pymysql
import hashlib
import smtplib
from email.mime.text import MIMEText
import base64




#windows
windows = Tk()
windows.title('Login Screen')
windows.resizable(0,0)
windows.geometry('510x380+200+180')


#database

def send_email(receiver_email, new_password):
    # Email details
    sender_email = 'gvineeth1910@gmail.com'
    sender_password = 'gvcfurqacktadfpt'
    subject = 'Password Change'
    message = f'Your new password is: {new_password}'

    # Create the email message
    email = MIMEText(message)
    email['Subject'] = subject
    email['From'] = sender_email
    email['To'] = receiver_email

    try:
        # Create a secure SSL connection to the SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            # Login to the email account
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, receiver_email, email.as_string())

        print('Email sent successfully.')
    except Exception as e:
        print(f'An error occurred while sending the email: {str(e)}')

# Example usage
receiver_email = 'vineethgajjela04@gmail.com'
new_password = ''

def forgot():
    send_email(receiver_email,new_password)
    windows.destroy()
    import Forgot_password

def user():

    windows.destroy()
    import Username


# Function to check password strength
def check_password_strength(password):
    # Check if the password meets the required conditions
    if len(password) < 8:
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    return True


def login():
    if emailEntry.get() == '':
        messagebox.showerror('Alert!', 'Please enter your email')

    elif passwordEntry.get() == '':
        messagebox.showerror('Alert!', 'Please enter your password')

    else:
        salt = '5gz'
        password_1 = passwordEntry.get() + salt
        password_hash = hashlib.md5(password_1.encode()).hexdigest()

        # Check password strength
        password_strength = check_password_strength(passwordEntry.get())
        if not password_strength:
            messagebox.showerror('Alert!', 'Password does not meet the strength requirements')
            return

        db = pymysql.connect(host='localhost', user='root', password='Vineeth04!',database='Personal_registration_form')
        cur=db.cursor()
        query='select * from p_details where password=%s'
        cur.execute(query,(password_hash))

        row=cur.fetchone()
        if row == None:
            messagebox.showerror('Alert!','Incorrect Email and Password')
            return
        else:
            # Base64 encode the username and password
            username = emailEntry.get().encode('utf-8')
            password = passwordEntry.get().encode('utf-8')
            encoded_username = base64.b64encode(username).decode('utf-8')
            encoded_password = base64.b64encode(password).decode('utf-8')

            messagebox.showinfo('Success', 'Successful Login')
            # Navigate to the next page here
            windows.destroy()  # Destroy the current window
            import Management_system




        #check button configuration
def show():
    passwordEntry.configure(show='*')
    check.configure(command=hide, text='')

def hide():
    passwordEntry.configure(show='')
    check.configure(command=show, text='')

def On_FocusEmailIn(event):
    emailEntry.delete(0,END)


def On_FocusEmailOut(event):
    name=emailEntry.get()
    if name == '':
        emailEntry.insert(0,'EMAIL')


def On_FocusPasswdIn(event):
    passwordEntry.delete(0, END)


def On_FocusPasswdOut(event):
    password=passwordEntry.get()
    if password == '':
        passwordEntry.insert(0, 'PASSWORD')


def newone():
    windows.destroy()
    import Personal_Registration_form







#frame
frame=Frame(windows, width=245000, height=244900,bg='black')
frame.place(x=0,y=0)

#Labels
LogoImage = PhotoImage(file='gmail (1).png')
emailLabel = Label(frame, text='Email : ', fg='blue', image=LogoImage, compound=LEFT, bg='black', font=('Calibre', 14, 'bold'))
emailLabel.grid(row=1, column=0, pady=20, padx=3)

passwordImage = PhotoImage(file='lock (1).png')
passwordLabel = Label(frame, image=passwordImage, compound=LEFT, fg='blue', bg='black', text='Password : ', font=('Calibre', 14, 'bold'))
passwordLabel.grid(row=3, column=0, pady=10, padx=3)


#Entryfields
emailEntry = Entry(frame, width=39, bd=3)
emailEntry.grid(row=1, column=2, columnspan=2, padx=57)

passwordEntry = Entry(frame, width=39, bd=3)
passwordEntry.grid(row=3, column=2, columnspan=2)

donthaveaccntLabel = Label(frame, text="Don't have an account?", fg='sky blue', bg='black', padx=4, font=('Harrington',9,'bold'))
donthaveaccntLabel.place(x=5,y=200)


createnewaccnt = Button(frame, width=15, text='Create one', border=0, bg='white', cursor='hand2', fg='black', font=('tahoma',8,'bold'),command=newone)
createnewaccnt.place(x=10,y=240)

fogotpw = Button(frame, text='forgot password', fg='Blue', border=0, cursor='hand2', bg='black', font=('Harrington',9, 'bold'),command=forgot)
fogotpw.place(x=360, y=150)

fogotus = Button(frame,text='forgot username', fg='Blue', border=0, cursor='hand2', bg='black', font=('Harrington',9,'bold'),command=user)
fogotus.place(x=360, y=180)

# Login button
loginbtn = Button(frame, text='Login', bg='Violet', pady=10, width=23, fg='White', font=('open sans',9,'bold'), cursor='hand2', border=0, borderwidth=5, command=login)
loginbtn.grid(row=9, columnspan=5, pady=30)

#checkbutton/box
check = Checkbutton(frame, text='', bg='black', command=show)
check.place(x=470, y=120)

#string of information
emailEntry.insert(0,'@email.com')
passwordEntry.insert(0,'password')

#events/binding
emailEntry.bind('<FocusIn>', On_FocusEmailIn)
emailEntry.bind('<FocusOut>', On_FocusEmailOut)


passwordEntry.bind('<FocusIn>', On_FocusPasswdIn)
passwordEntry.bind('<FocusOut>', On_FocusPasswdOut)






windows.mainloop()

from tkinter import *


#windows size
windows = Tk()
windows.title('Management System')
windows.geometry('1200x1200+0+0')
windows.resizable(0,0)

frame = Frame(windows,width=1200,height=1200,bg='black',bd=8)
frame.place(x=0,y=0)

heading = Label(frame,text='Management_System',fg='blue',bg='black',font=('Calibre',20,'bold'))
heading.place(x=450, y=3)

windows.mainloop()
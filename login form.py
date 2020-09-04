try:
    from Tkinter import *
except ImportError:
    from tkinter import *

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from subprocess import call
import time
import datetime
import calendar

class Login_form:
    def __init__(self, window):
        self.wn = window
        self.wn.title("Login Form")
        self.wn.geometry("1900x851")

        self.lb_Heading = Label(self.wn, text='login Form', font=('arial', 20, 'bold'), fg='silver').place(x=10,y=10)

# -----------------------image-------------------

        self.wn.bg=ImageTk.PhotoImage(file='ooo.png')
        self_bg_image=Label(self.wn,image=self.wn.bg)
        self_bg_image.place(x=0,y=0)

        self.wn.pg=ImageTk.PhotoImage(file='page.PNG')
        self_pg_image=Label(self.wn,image=self.wn.pg,width=350,height=350)
        self_pg_image.place(x=465,y=250)

        self.wn.cg = ImageTk.PhotoImage(file='rsz_1n.png')
        self_cg_image = Label(self.wn, image=self.wn.cg,  bd=0)
        self_cg_image.place(x=520, y=330)

        self.wn.ng = ImageTk.PhotoImage(file='rsz_pass.png')
        self_ng_image = Label(self.wn, image=self.wn.ng, bd=0)
        self_ng_image.place(x=520, y=410)

        self.title=Label(self.wn,text='Welcome to Annapurna hotel',font=('times and roman',30,'bold'), bd=10,bg='skyblue')
        self.title.place(x=0,y=5,relwidth=1)

        #===================time=================

        def clock():
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))

            dd = str(time.strftime("%d"))
            mm = int(time.strftime("%m"))
            mm = calendar.month_name[mm]
            yy = datetime.datetime.now()

            self.Date.config(text=dd)
            self.mon.config(text=str(mm))
            self.year.config(text=str(yy.year))

            if int(h)>12 and int(m)>0:
                self.noon.config(text="PM")
            if int(h)>12:
                 self.h=str((int(h)-12))

            self.hr.config(text=h)
            self.min.config(text=m)
            self.sec.config(text=s)

            self.hr.after(200,clock)

        self.hr = Label(self.wn, text='12', font=("times new roman", 20, "bold"), bg="#087587", fg="black")
        self.hr.place(x=520, y=100, width=50, height=50)

        self.hr2 = Label(self.wn, text="HOUR", font=("times new roman", 10,"bold"),bg="#087587", fg="white")
        self.hr2.place(x=520, y=160, width=50)

        self.Date = Label(self.wn, text="DATE", font=("times new roman", 10, "bold"), bg="#087587", fg="white")
        self.Date.place(x=520, y=190, width=50)

        self.min = Label(self.wn, text='12', font=("times new roman", 20, "bold"), bg="#087587", fg="black")
        self.min.place(x=580, y=100, width=50, height=50)

        self.min2 = Label(self.wn, text="MINUTE", font=("times new roman", 10, "bold"), bg="#087587", fg="white")
        self.min2.place(x=580, y=160, width=50)

        self.mon = Label(self.wn, text="MONTH", font=("times new roman", 10, "bold"), bg="#087587", fg="white")
        self.mon.place(x=580, y=190, width=53)

        self.sec = Label(self.wn, text='12', font=("times new roman", 20, "bold"), bg="#DF002A", fg="black")
        self.sec.place(x=640, y=100, width=50, height=50)

        self.sec2 = Label(self.wn, text="SECOND", font=("times new roman", 10, "bold"), bg="#DF002A", fg="white")
        self.sec2.place(x=640, y=160, width=50)


        self.year = Label(self.wn, text="Year", font=("times new roman", 10, "bold"), bg="#DF002A", fg="white")
        self.year.place(x=640, y=190, width=50)

        self.noon = Label(self.wn, text='AM', font=("times new roman", 20, "bold"), bg="#DF002A", fg="black")
        self.noon.place(x=700, y=100, width=50, height=50)

        self.noon2 = Label(self.wn, text="NOON", font=("times new roman", 10, "bold"), bg="#DF002A", fg="white")
        self.noon2.place(x=700, y=160, width=50)

        self.current = Label(self.wn, text="DATE", font=("times new roman", 10, "bold"), bg="#DF002A", fg="white")
        self.current.place(x=700, y=190, width=50)

        clock()

        #====================Label=====================
        self.lb_username = Label(self.wn, text='Username', font=('arial', 15, 'bold'))
        self.lb_username.place(x=550,y=330)

        self.ent_username = Entry(self.wn, font=('arial', 15, 'bold'), fg='black')
        self.ent_username.place(x=515,y=370)

        self.lb_pass = Label(self.wn, text='Password', font=('arial', 15, 'bold'))
        self.lb_pass.place(x=550, y=410)

        self.ent_pass = Entry(self.wn, font=('arial', 15, 'bold'), show='*', fg='black')
        self.ent_pass.place(x=515, y=450)

        self.btn_log=Button(self.wn, text="login", width=20,font=('arial', 15, 'bold'), bg='light blue',command=self.login)
        self.btn_log.place(x=510,y=500)

    def login(self):
        if self.ent_username.get() == "" or self.ent_username.get() == "":
            messagebox.showerror('Error', 'All fields are required!!')

        elif self.ent_username.get() == 'admin' and self.ent_pass.get() == 'admin':
            messagebox.showinfo('Successfull', f"welcome {self.ent_username.get()}")

            call(["python", "main1.py"])

        else:
            messagebox.showerror('Error', "All fields are required!!")

wn=Tk()
Login_form(wn)
wn.mainloop()

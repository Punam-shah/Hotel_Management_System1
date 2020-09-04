from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from assignment.qry import Check_in


class check_out:
    def __init__(self, window):
        self.window = window
        self.window.title("CHECK OUT")
        self.window.geometry("880x641+504+123")

        self.check_out = Check_in()

        self.name = StringVar()
        self.room_no = StringVar()
        self.date = StringVar()
        self.time = StringVar()
        self.time_c = StringVar()
        #-----------------------------------
        self.f1 = LabelFrame(self.window, width=400, height=500,text="GUEST INFORMATION")
        self.f1.pack(side=LEFT, padx=20, pady=10)

        self.f2 = LabelFrame(self.window, width=400,height=495, bg='white')
        self.f2.pack(side=RIGHT, padx=21, pady=10)
        #-----------------label-------------------------


        self.info_label = Label(self.f2, width=56, height=2, bg='white', anchor=W)
        self.info_label.place(x=0, y=30)

        self.info_label1 = Label(self.f2, width=56, height=2, bg='white', anchor=W)
        self.info_label1.place(x=1, y=0)

        self.lb = Label(self.f1, text="Date:", font=('arial', 12, 'bold'))
        self.lb.place(x=10, y=10)
        self.ent = Entry(self.f1, textvariable=self.date, width=20)
        self.ent.place(x=85, y=10)

        self.ent.bind('<Button-1>', self.date1)



        self.lb = Label(self.f1, text="Time", font=('arial', 12, 'bold'))  # Date Label
        self.lb.place(x=10, y=40)
        self.ent0 = Entry(self.f1, textvariable=self.time, width=8)
        self.ent0.place(x=85, y=40)


        self.time1 = ttk.Combobox(self.f1, textvariable=self.time_c, width=6)

        # Adding combobox drop down list
        self.time1['values'] = ('PM',
                               'AM')

        self.time1.place(x=140, y=40)



        self.lb1 = Label(self.f1, text="Enter Guest Name:", font=('verdana', 15, 'bold'))
        self.lb1.place(x=60, y=140)
        self.ent1 = Entry(self.f1, textvariable=self.name, width=20, font=('verdana'))
        self.ent1.place(x=50, y=170)



        self.lb2 = Label(self.f1, text="Enter Guest Room_no:", font=('verdana', 15, 'bold'))
        self.lb2.place(x=60, y=200)
        self.ent2 = Entry(self.f1, textvariable=self.room_no, font=("verdana"), width=20)
        self.ent2.place(x=50, y=230)



        #--------buttom-----------

        # self.btn_checkout = Button(self.f1, text='CHECK OUT', font=('verdana', 15, 'bold'), command=self.checkout)
        # self.btn_checkout.place(x=100, y=250)
        #
        self.photo_out = PhotoImage(file="pu.PNG")
        self.photo_out_lable = Label(self.window, image=self.photo_out, bg="white")  # check out
        self.photo_out_lable.image = self.photo_out
        self.photo_out_lable.place(x=100, y=450)
        self.out = Button(height=60, width=220, image=self.photo_out, command=self.checkout)
        self.out.place(x=80, y=450)

        self.back_btn = Button(self.window, text="Back", font=('arial', 12, 'bold'), command=self.window.destroy)  # back button
        self.back_btn.place(x=800)

        self.d_check_out = dict()
        for i in self.check_out.show_all():
            self.d_check_out[i[2]] = i[7]

        print(self.d_check_out)


    def date1(self, event):
        self.top = Toplevel(self.f1)
        self.cal = Calendar(self.top, selectmode="day", year=2020, month=8, day=30)
        self.cal.pack()

        def date2():
            self.ent.insert(0, self.cal.get_date())
            self.top.destroy()

        self.cal1 = Button(self.top, text="Enter", command=date2)
        self.cal1.pack()

        print(self.d_check_out)


    def checkout(self):
        name = self.name.get()
        room = (self.room_no.get())
        date = self.date.get()+"-"+self.time.get()+"-"+self.time_c.get()
        # time = self.time.get()
        # data = [i[2] for i in self.check_out.show_all()]
        # data_2 = [i[7] for i in self.check_out.show_all()]
        # print(data)
        # print(data_2)


        if name in self.d_check_out:
            if room in self.d_check_out[name]:

                self.info_label['text'] = ('HAVE A NICE DAY'+' ' + name+' '+'Please visit again')
                self.info_label1['text'] = ('Check out time' + ' ' + date + ' ' + 'Thank You For visiting')
                self.check_out.check_out(date, name, room)
                self.check_out.delete1(name)
                self.check_out.delete2(name, room)

        else:
            messagebox.showerror("Error", "ENTER VALID DETAILS")
            self.info_label['text'] = ''
            self.info_label1['text'] = ''





win = Tk()
check_out(win)
win.mainloop()


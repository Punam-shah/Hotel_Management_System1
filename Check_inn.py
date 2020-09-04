try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk



from tkinter import *
from tkcalendar import *
from tkinter import ttk
from tkinter import messagebox
#import unittest


from assignment.qry import Check_in


class Check_in_info:
    def __init__(self, window):
        self.window = window
        self.window.title("CHECK INN")
        self.window.geometry("1069x742+50+-1")
        self.update_index = ""
        self.check = Check_in()

        self.name = StringVar()
        self.time = StringVar()
        self.date = StringVar()
        self.time_c = StringVar()
        self.address = StringVar()
        self.number = StringVar()
        self.day = StringVar()
        self.room_no = StringVar()
        self.room_type_var = StringVar()
        self.payment_var = StringVar()

        self.value = ""


        self.f1 = LabelFrame(window, text="GUEST INFORMATION")
        self.f1.pack(fill="both", expand="yes", padx=20, pady=10)

        self.f2 = LabelFrame(window)
        self.f2.pack(fill="both", expand="yes", padx=25, pady=10)

        self.canvas = Canvas(self.f2)
        # self.canvas.pack(side=LEFT)

        # Tree view
        self.trv = ttk.Treeview(self.f2, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings",height="10")
        self.trv.place(x=0, y=0)

        self.trv.column(1, width=130)
        self.trv.column(2, width=130)
        self.trv.column(3, width=130)
        self.trv.column(4, width=120)
        self.trv.column(5, width=130)
        self.trv.column(6, width=130)
        self.trv.column(7, width=130)
        self.trv.column(8, width=110)
        self.trv.heading(1, text="DATE/TIME")
        self.trv.heading(2, text="NAME")
        self.trv.heading(3, text="ADDRESS")
        self.trv.heading(4, text="PHONE NUMBER")
        self.trv.heading(5, text="NUMBER OF DAYS")
        self.trv.heading(6, text="ROOM NO")
        self.trv.heading(7, text="ROOM TYPE")
        self.trv.heading(8, text="PAYMENT BY")
        #
        # self.trv.pack(side=LEFT, fill=BOTH)
        # self.scrollbar.config(command=self.trv.yview)

        # guest information

        self.lb1 = Label(self.f1, text="Name", font=('arial', 12, 'bold'))  # Name Label
        self.lb1.grid(row=0, column=0)
        self.ent1 = Entry(self.f1, textvariable=self.name)
        self.ent1.grid(row=0, column=1)

        self.lb7 = Label(self.f1, text="Date", font=('arial', 12, 'bold'))  # date
        self.lb7.place(x=400, y=50)
        self.ent6 = Entry(self.f1, textvariable=self.date)
        self.ent6.place(x=450, y=50)

        self.lb = Label(self.f1, text="Time", font=('arial', 12, 'bold'))  # Date Label
        self.lb.place(x=400, y=0)
        self.ent = Entry(self.f1, textvariable=self.time, width=6)
        self.ent.place(x=450, y=0)

        self.time1 = ttk.Combobox(self.f1, width=5, textvariable=self.time_c)

        # Adding combobox drop down list
        self.time1['values'] = ('PM',
                               'AM')

        self.time1.place(x=500, y=0)





        self.lb2 = Label(self.f1, text="Address", font=('arial', 12, 'bold'))  # Address Label
        self.lb2.grid(row=1, column=0)
        self.ent2 = Entry(self.f1, textvariable=self.address)
        self.ent2.grid(row=1, column=1)

        self.lb3 = Label(self.f1, text="Phone number", font=('arial', 12, 'bold'))  # Phone no
        self.lb3.grid(row=2, column=0)
        self.ent3 = Entry(self.f1, textvariable=self.number)
        self.ent3.grid(row=2, column=1)
        self.ent3.insert(0,"+977")


        self.lb4 = Label(self.f1, text="Number of days", font=('arial', 12, 'bold'))  # Checkin days
        self.lb4.grid(row=3, column=0)
        self.ent4 = Entry(self.f1, textvariable=self.day)
        self.ent4.grid(row=3, column=1)

        self.lb5 = Label(self.f1, text="Enter room number", font=('arial', 12, 'bold'))  # Room no
        self.lb5.grid(row=4, column=0)

        self.room_choose = ttk.Combobox(self.f1, width=17, textvariable=self.room_no, state = 'readonly')

        # Adding combobox drop down list
        self.room_choose['values'] = (' 101',
                                      '102',
                                      ' 103',
                                      ' 104',
                                      ' 105',
                                      ' 106',
                                      '107',
                                      ' 108',
                                      ' 109',
                                      ' 110',
                                      '111',
                                      '112',
                                      '113',
                                      '114',
                                      '115',
                                      '116',
                                      '117',
                                      '118',
                                      '119',
                                      '120',
                                      '121',
                                      '122',
                                      '123',
                                      '124',
                                      '125',
                                      '126',
                                      '127',
                                      '128',
                                      '129',
                                      '120')

        self.room_choose.grid(row=4, column=1)
        self.room_choose.current()


        # -----------------RadioButton-----------

        self.radio_btn1 = Radiobutton(self.f1, text="DELUXE", variable=self.room_type_var, font=('arial', 12, 'bold'),
                                      value='Deluxe', tristatevalue='x', command = self.price)  # DELUXE
        self.radio_btn1.grid(row=6, column=2)

        self.radio_btn2 = Radiobutton(self.f1, text="GENERAL", variable=self.room_type_var, font=('arial', 12, 'bold'),
                                      value='General', tristatevalue='x', command = self.price)  # GENERAL
        self.radio_btn2.grid(row=6, column=0)

        self.radio_btn3 = Radiobutton(self.f1, text="FULL DELUXE", variable=self.room_type_var,
                                      font=('arial', 12, 'bold'), value='Full_Deluxe', tristatevalue='x', command = self.price)  # FULL DELUXE
        self.radio_btn3.grid(row=6, column=4)

        self.radio_btn4 = Radiobutton(self.f1, text="JOINT", variable=self.room_type_var, font=('arial', 12, 'bold'),
                                      value='Joint', tristatevalue='x', command = self.price)  # JOINT
        self.radio_btn4.grid(row=6, column=1, padx=5, pady=5)

        self.lb5 = Label(self.f1, text="CHOOSE PAYMENT METHOD", font=('arial', 12, 'bold'))  # PAYMENT
        self.lb5.grid(row=8, column=1, padx=20, pady=10)

        self.radio_btn5 = Radiobutton(self.f1, text="By cash", variable=self.payment_var, font=('arial', 12, 'bold'),
                                      value='Cash', tristatevalue='y', command = self.payment)  # CASH
        self.radio_btn5.grid(row=9, column=0, padx=20, pady=10)

        self.radio_btn6 = Radiobutton(self.f1, text="By credit/debit card", variable=self.payment_var,
                                      font=('arial', 12, 'bold'), value='Card', tristatevalue='y', command=self.payment)  # CARD
        self.radio_btn6.grid(row=9, column=1, padx=20, pady=10)





        # BUTTONS

        self.up_btn = Button(self.f1, text="Update Guest", font=('arial', 12, 'bold'),
                             command=self.update_but_func)  # update button
        self.up_btn.grid(row=10, column=1, padx=20, pady=10)

        self.add_btn = Button(self.f1, text="Add Guest", font=('arial', 12, 'bold'),
                              command=self.add_but_func)  # add button
        self.add_btn.grid(row=10, column=0)

        self.delete_btn = Button(self.f1, text="Delete Guest", font=('arial', 12, 'bold'),
                                 command=self.delete_but_func)  # delete button
        self.delete_btn.grid(row=10, column=2)

        self.back_btn = Button(self.f1, text="Back", font=('arial', 12, 'bold'),
                               command=self.window.destroy)  # back button
        self.back_btn.grid(row=1, column=11)



        self.show_guest_tree()

        self.ent6.bind('<Button-1>', self.date_btn)

    def date_btn(self, event):
        self.top =Toplevel(self.f1)
        self.cal = Calendar(self.top, selectmode="day", year=2020, month=8, day=30)
        self.cal.pack()

        def date():
            self.ent6.insert(0,self.cal.get_date())
            self.top.destroy()

        self.cal1 = Button(self.top, text = "Enter", command = date)
        self.cal1.pack()

    def add_but_func(self):
        name = self.name.get()
        date = self.date.get()
        address = self.address.get()
        number = self.number.get()
        days = self.day.get()
        room = self.room_no.get()
        room_type = self.room_type_var.get()
        payment = self.payment_var.get()
        price = payment+"-"+str(self.value)
        time = date+"-"+self.time.get()+"-"+self.time_c.get()
        print(self.value)

        if name == "" or address == "" or date == "" or self.time.get() == "" or number == "" or days == "" or room == "" or room_type == "" or payment == "" :
            messagebox.showerror("error", 'please fill up all details')
        elif len(number) >= 15 or len(number) < 14:
            messagebox.showerror('error', 'invalid number')
        else:
            if self.check.add(time, name, address, number, days, price):
                if self.check.add_room(name, room, room_type):
                    if self.check.add_guest(name, room, time):
                        messagebox.showinfo('ADDED', 'Guest Info Added', parent=self.window)
                        self.show_guest_tree()
                        self.ent1.delete(0, END)
                        self.ent2.delete(0, END)
                        self.ent3.delete(0, END)
                        self.ent3.insert(0, '+977')
                        self.ent4.delete(0, END)
            else:
                messagebox.showerror('Error', 'Cannot add info!!!', parent=self.window)

    def delete_but_func(self):
        name = self.name.get()
        room = self.room_no.get()
        if self.update_index == "":
            messagebox.showerror("Error", "please select a row first", parent=self.window)
        elif self.update_index != "":
            self.check.delete1(name)
            self.check.delete2(name, room)

            messagebox.showinfo("DELETED", "selected row deleted", parent=self.window)
            self.show_guest_tree()
            self.update_index = " "
            self.ent1.delete(0, END)
            self.ent.delete(0, END)
            self.ent6.delete(0,END)
            self.ent2.delete(0, END)
            self.ent3.delete(0, END)
            self.ent3.insert(0,'+977')
            self.ent4.delete(0, END)
            self.room_choose.delete(0, END)
            self.radio_btn1.deselect()
            self.radio_btn2.deselect()
            self.radio_btn3.deselect()
            self.radio_btn4.deselect()
            self.radio_btn5.deselect()
            self.radio_btn6.deselect()

        else:
            messagebox.showerror("Error", "Couldn't Update Info", parent=self.window)

    def update_but_func(self):
        if self.update_index == "":
            messagebox.showerror("Error", "please select a row first", parent=self.window)
        else:
            name = self.name.get()
            date = self.date.get()
            address = self.address.get()
            number = self.number.get()
            days = self.day.get()
            room = self.room_no.get()
            room_type = self.room_type_var.get()
            payment = self.payment_var.get()
            price = payment + "-" + str(self.value)
            time = date + "-" + self.time.get() + "-" + self.time_c.get()


            if self.check.update(self.update_index, time, name, address, number, days, price):
                if self.check.update_room(self.update_index, name, room, room_type):
                    messagebox.showinfo("UPDATED", "GUEST INFO UPDATED", parent=self.window)
                    self.show_guest_tree()
                    self.update_index = " "
            else:
                messagebox.showerror("Error", "Couldn't Update Info", parent=self.window)


    def show_guest_tree(self):
        self.trv.delete(*self.trv.get_children())
        data = self.check.show_all()
        print(data)
        for i in data:
            self.trv.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5], i[7], i[8], i[6]))
        self.trv.bind("<Double-1>", self.on_item_select)

    def on_item_select(self, event):
        selected_row = self.trv.selection()[0]
        selected_item = self.trv.item(selected_row, 'values')
        self.update_index = self.trv.item(selected_row, 'text')
        print(self.update_index)
        a = selected_item[0].split("-")

        self.ent6.delete(0, END)
        self.ent6.insert(0, a[0])
        self.time1.delete(0, END)
        self.time1.insert(0, a[2])
        self.ent.delete(0, END)
        self.ent.insert(0, a[1])
        self.ent1.delete(0, END)
        self.ent1.insert(0, selected_item[1])
        self.ent2.delete(0, END)
        self.ent2.insert(0, selected_item[2])
        self.ent3.delete(0, END)
        self.ent3.insert(0, selected_item[3])
        self.ent4.delete(0, END)
        self.ent4.insert(0, selected_item[4])
        self.room_choose.delete(0, END)
        self.room_choose.insert(0, selected_item[5])
        # self.radio_btn1.select()
        if selected_item[6] == 'Deluxe':
            self.radio_btn1.select()
            self.radio_btn2.deselect()
            self.radio_btn3.deselect()
            self.radio_btn4.deselect()

        elif selected_item[6] == 'General':
            self.radio_btn2.select()
            self.radio_btn1.deselect()
            self.radio_btn3.deselect()
            self.radio_btn4.deselect()

        elif selected_item[6] == 'Full_Deluxe':
            self.radio_btn3.select()
            self.radio_btn1.deselect()
            self.radio_btn2.deselect()
            self.radio_btn4.deselect()

        elif selected_item[6] == 'Joint':
            self.radio_btn4.select()
            self.radio_btn1.deselect()
            self.radio_btn2.deselect()
            self.radio_btn3.deselect()

        p = selected_item[7].split("-")

        if p[0] == 'Cash':
            self.radio_btn5.select()
            self.radio_btn6.deselect()

        elif p[0] == 'Card':
            self.radio_btn6.select()
            self.radio_btn5.deselect()

        else:
            return

    def price(self):
        if self.room_type_var.get() == "General":
            self.value = eval("5000*%s" % self.day.get())

        elif self.room_type_var.get() == "Joint":
            self.value = eval("10000*%s" % self.day.get())

        elif self.room_type_var.get() == "Deluxe":
            self.value = eval("15000*%s" % self.day.get())

        elif self.room_type_var.get() == "Full_Deluxe":
            self.value = eval("20000*%s" % self.day.get())

    def payment(self):
        if self.payment_var.get() == "Cash":
            messagebox.showinfo("payment", "YOUR TOTAL BILL IS Rs." + str(self.value))

        elif self.payment_var.get() == "Card":
            messagebox.showinfo("payment", "YOUR TOTAL BILL IS Rs." + str(self.value))

        else:
            messagebox.showerror("ERROR", "CANNOT COMPLETE YOUR REQUEST ")



win = Tk()
Check_in_info(win)
win.mainloop()


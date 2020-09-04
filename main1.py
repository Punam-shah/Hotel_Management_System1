try:
    from Tkinter import *
except ImportError:
    from tkinter import *


from tkinter import *
from subprocess import call
from PIL import ImageTk


class hotel_management:
    def __init__(self, window):
        self.window = window
        self.window.title("WELCOME TO ANNAPURNA")
        self.window.geometry("1069x742")

        try:


            self.window.bg = ImageTk.PhotoImage(file='h.jpg')
            self.bg_image = Label(self.window, image=self.window.bg)
            self.bg_image.place(x=0, y=0)

        except FileNotFoundError:
            print("File not found")
            self.bg_image = Label(self.window, width=1069, height=742, bg='teal')
            self.bg_image.place(x=0, y=0)

        self.photo_inn = PhotoImage(file="1.PNG")
        self.photo_inn_lable = Label(self.window, image=self.photo_inn, bg="white")     # check inn
        self.photo_inn_lable.image = self.photo_inn
        self.photo_inn_lable.place(x=400, y=150)
        self.inn = Button(height=60, width=350, image=self.photo_inn,command=self.btn_check_inn)
        self.inn.place(x=400, y=150)

        self.photo_info = PhotoImage(file="2.PNG")
        self.photo_info_lable = Label(self.window, image=self.photo_info, bg="white")       #show guest list
        self.photo_info_lable.image = self.photo_info
        self.photo_info_lable.place(x=400, y=240)
        self.info = Button(height=60, width=350, image=self.photo_info, command=self.btn_guestlist)
        self.info.place(x=400, y=220)

        self.photo_out = PhotoImage(file="4.PNG")
        self.photo_out_lable = Label(self.window, image=self.photo_out, bg="white")         #check out
        self.photo_out_lable.image = self.photo_out
        self.photo_out_lable.place(x=400, y=290)
        self.out = Button(height=60, width=350, image=self.photo_out, command=self.btn_check_out)
        self.out.place(x=400, y=290)

        self.photo_gu = PhotoImage(file="6.PNG")
        self.photo_gu_lable = Label(self.window, image=self.photo_gu, bg="white")       #GET INFO OF ANY GUEST
        self.photo_gu_lable.image = self.photo_gu
        self.photo_gu_lable.place(x=400, y=360)
        self.gu = Button(height=60, width=350, image=self.photo_gu, command=self.btn_guest_info)
        self.gu.place(x=400, y=360)

        self.photo_ex = PhotoImage(file="7.PNG")
        self.photo_ex_lable = Label(self.window, image=self.photo_ex, bg="white")           #exit
        self.photo_ex_lable.image = self.photo_ex
        self.photo_ex_lable.place(x=400, y=430)
        self.ex = Button(height=60, width=350, image=self.photo_ex, command=quit)
        self.ex.place(x=400, y=430)

        self.photo_x = PhotoImage(file="WEL.PNG")
        self.photo_x_lable = Label(self.window, height=60, width=750,image=self.photo_x, bg='white')
        self.photo_x_lable.image = self.photo_x
        self.photo_x_lable.place(x=200,  y=10)


    def btn_check_inn(self):
        call(["python", "Check_inn.py"])

    def btn_guestlist(self):
        call(["python", "info.py"])

    def btn_check_out(self):
        call(["python", "Check_out.py"])

    def btn_guest_info(self):
        call(["python", "guest_info.py"])






window = Tk()
hotel_management(window)
window.mainloop()


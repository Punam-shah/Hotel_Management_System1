from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from assignment.qry import Check_in

class Guest_info:
    def __init__(self, window):
        self.window = window
        window.title("GET INFORMATION")
        window.geometry("1069x742")

        self.info = Check_in()
        #----------------Searching algo----------
        self.d = dict()
        for i in range (len(self.info.show_all())):
            self.d[i] = [self.info.show_all()[i][1:]]

        self.name = [i[2] for i in self.info.show_all()]

        #---------frame--------

        self.f1 = LabelFrame(window, bg='gray90')
        self.f1.pack(fill="both", expand="yes", padx=20, pady=10)

        self.f2 = LabelFrame(window)
        self.f2.pack(fill="both", expand="yes", padx=21, pady=10)

        #--------------heading-------------

        self.head1 = Message(self.window, text="GET INFO HERE ..!!", font=('verdana', 20, 'bold'), width=450 )
        self.head1.place(x=375,y=50)

        self.head2 = Message(self.window, text="ENTER GUEST'S NAME  :", font=('verdana', 20, 'bold'), width=450)
        self.head2.place(x=150, y=100)

        self.ent_head2 = Entry(self.window, font=("verdana"))
        self.ent_head2.place(x=615, y=110)



        #-----------treeview----------

        self.trv = ttk.Treeview(self.f2, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="15")
        self.trv.place(x=0, y=0)

        self.trv.column(1, width=100)
        self.trv.column(2, width=130)
        self.trv.column(3, width=130)
        self.trv.column(4, width=130)
        self.trv.column(5, width=130)
        self.trv.column(6, width=130)
        self.trv.column(7, width=130)
        self.trv.column(8, width=140)
        self.trv.heading(1, text="Date")
        self.trv.heading(2, text="NAME")
        self.trv.heading(3, text="ADDRESS")
        self.trv.heading(4, text="PHONE NUMBER")
        self.trv.heading(5, text="NUMBER OF DAYS")
        self.trv.heading(6, text="ROOM NO")
        self.trv.heading(7, text="ROOM TYPE")
        self.trv.heading(8, text="PAYMENT BY")

        #---------------button----------

        self.sub_but = Button(self.window, text="SEARCH", font=("verdana", 20,"bold"), command=self.search_func)
        self.sub_but.place(x=400, y=200)



        self.back_btn = Button(self.f1, text="Back", font=('arial', 12, 'bold'),command=self.window.destroy)  # back button
        self.back_btn.place(x=950, y=0)


    def search_func(self):
        self.input = self.ent_head2.get()
        if self.input == '':
            messagebox.showerror('ERROR', 'CANNOT PROCESS YOUR REQUEST...')

        elif self.input != '':
            for i in range(len(self.name)):
               if self.input == self.name[i]:
                   self.search = self.d[self.name.index(self.input)]
                   messagebox.showinfo('FOUND', 'GUEST FOUND')
                   self.show_guest_tree()


        else:

            messagebox.showerror('ERROR', 'CANNOT PROCESS YOUR REQUEST...')


    def show_guest_tree(self):
        self.input = self.ent_head2.get()
        self.trv.delete(*self.trv.get_children())

        self.trv.delete(*self.trv.get_children())

        for i in self.search:
            self.trv.insert("", "end", text=i[0], value=(i[0], i[1], i[2], i[3], i[4], i[6], i[7], i[5]))




window=Tk()
Guest_info(window)
window=mainloop()

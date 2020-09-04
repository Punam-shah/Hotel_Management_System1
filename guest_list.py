from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from assignment.qry import Check_in


class guest_list:
    def __init__(self, window):
        self.window = window
        window.title("LIST OF ALL GUEST")
        window.geometry("880x641+504+123")

        self.list = Check_in()

        self.head1 = Message(self.window, text="List of All Guest", font=('verdana', 20, 'bold'), width=450)
        self.head1.place(x=300)

        self.f1 = LabelFrame(window, width=430, height=500, bg="black")
        self.f1.pack(side=LEFT, padx=10, pady=5)

        self.trv = ttk.Treeview(self.f1, columns=(1), show="headings", height=500)
        self.trv.place(x=0, y=0)
        self.trv.column(1, width=430)
        self.trv.heading(1, text="Name")


        self.f2 = LabelFrame(window, width=430, height=500, bg="black")
        self.f2.pack(side=RIGHT, padx=10, pady=5)

        self.trv2 = ttk.Treeview(self.f2, columns=(1), show="headings", height=500)
        self.trv2.place(x=0, y=0)
        self.trv2.column(1, width=430)
        self.trv2.heading(1, text="Room Number")

        #--------------button---------------

        self.back_btn = Button(self.window, text="Back", font=('arial', 12, 'bold'),command=self.window.destroy)  # back button
        self.back_btn.place(x=800, y=0)

        self.show_in_trv()

    def show_in_trv(self):
        self.trv.delete(*self.trv.get_children())
        self.trv2.delete(*self.trv2.get_children())

        data = self.list.show_guest()

        print(data)

        for i in data:
            self.trv.insert("", "end", text=i[0], value=(i[1]))
            self.trv2.insert("", "end", text=i[0], value=(i[2]))










win = Tk()
guest_list(win)
win.mainloop()

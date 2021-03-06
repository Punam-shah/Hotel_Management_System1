from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from assignment.qry import Check_in


class list:
    def __init__(self, window):
        self.window = window
        window.title("LIST OF ALL GUEST")
        window.geometry("880x500+504+123")

        self.list = Check_in()

        self.head1 = Message(self.window, text="List of All Guest", font=('verdana', 20, 'bold'), width=450)
        self.head1.place(x=300)

        self.f1 = LabelFrame(window, text="GUEST INFORMATION")
        self.f1.pack(fill="both", expand="yes", padx=40, pady=40)

        self.trv = ttk.Treeview(self.f1, columns=(1, 2, 3, 4), show="headings", height="500")
        self.trv.place(x=0, y=0)


        self.trv.column(1, width=200)
        self.trv.column(2, width=200)
        self.trv.column(3, width=200)
        self.trv.column(4, width=200)


        self.trv.heading(1, text="NAME")
        self.trv.heading(2, text="ROOM NO")
        self.trv.heading(3, text="CHECK INN")
        self.trv.heading(4, text="CHECK OUT")
        self.show_in_trv()


    def show_in_trv(self):
        self.trv.delete(*self.trv.get_children())

        data = self.list.show_guest()

        print(data)

        for i in data:
            self.trv.insert("", "end", text=i[0], value=(i[0], i[1], i[2], i[3]))






win = Tk()
list(win)
win.mainloop()

from tkinter import *
# import backend
from backend import Database

database = Database("bookstore.db")

class Window(object):

    def __init__(self,window):

        self.window = window
        self.window.wm_title("BookStore")

        t1 = Label(window,text ="Title" )
        t1.grid(row=0,column=0)

        self.title_entry = StringVar()
        self.e1 = Entry(window,textvariable = self.title_entry)
        self.e1.grid(row=0,column=1)

        t2 = Label(window,text ="Author" )
        t2.grid(row=0,column=2)

        self.author_entry = StringVar()
        self.e2 = Entry(window,textvariable = self.author_entry)

        self.e2.grid(row=0,column=3)

        t3 = Label(window,text ="Year" )
        t3.grid(row=1,column=0)

        self.year_entry = StringVar()
        self.e3 = Entry(window,textvariable = self.year_entry)
        self.e3.grid(row=1,column=1)

        t4 = Label(window,text ="ISBN" )
        t4.grid(row=1,column=2)

        self.isbn_entry = StringVar()
        self.e4 = Entry(window,textvariable = self.isbn_entry)
        self.e4.grid(row=1,column=3)

        b1 = Button(window,text="View All",width=12,command=self.view_command)
        b1.grid(row=2,column=3)

        b2 = Button(window,text="Search Entry",width=12,command=self.search_command)
        b2.grid(row=3,column=3)

        b3 = Button(window,text="Add Entry",width=12,command=self.add_command)
        b3.grid(row=4,column=3)

        b4 = Button(window,text="Update Selected",width=12,command=self.update_command)
        b4.grid(row=5,column=3)

        b5 = Button(window,text="Delete Selected",width=12,command=self.delete_command)
        b5.grid(row=6,column=3)

        b6 = Button(window,text="Close",width=12,command=window.destroy)
        b6.grid(row=7,column=3)

        self.t5 = Listbox(window,height=8,width=35)
        self.t5.grid(row=2,column=0,rowspan=6,columnspan=2)

        sb1= Scrollbar(window)
        sb1.grid(row=2,column=2,rowspan=6)

        self.t5.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.t5.yview)

        self.t5.bind('<<ListboxSelect>>',self.get_selected_record)


    def get_selected_record(self,event):
        # try:
            # global selected_tuple
        index=self.t5.curselection()[0]
        self.selected_tuple = self.t5.get(index)
        self.e1.delete(0,END)
        self.e1.insert(END,self.selected_tuple[1])
        self.e2.delete(0,END)
        self.e2.insert(END,self.selected_tuple[3])
        self.e3.delete(0,END)
        self.e3.insert(END,self.selected_tuple[4])
        self.e4.delete(0,END)
        self.e4.insert(END,self.selected_tuple[2])
        # except IndexError:
            # pass

    def delete_command(self):
        database.delete_entry(self.selected_tuple[0])

    def view_command(self):
        self.t5.delete(0,END)
        records = database.view_all()
        for record in records:
            self.t5.insert(END,record)

    def search_command(self):
        self.t5.delete(0,END)
        rows = database.search_entry(self.title_entry.get(),self.author_entry.get(),self.year_entry.get(),self.isbn_entry.get())
        for row in rows:
            self.t5.insert(END,row)

    def add_command(self):
        database.add_entry(self.title_entry.get(),self.isbn_entry.get(),self.author_entry.get(),self.year_entry.get())
        self.t5.delete(0,END)
        self.t5.insert(END,(self.title_entry.get(),self.isbn_entry.get(),self.author_entry.get(),self.year_entry.get()))

    def update_command(self):
        database.update_entry(self.selected_tuple[0],self.title_entry.get(),self.author_entry.get(),self.year_entry.get(),self.isbn_entry.get())

window = Tk()
Window(window)
window.mainloop()

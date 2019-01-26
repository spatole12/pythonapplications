from tkinter import *
import backend

def get_selected_record(event):
    try:
        global selected_tuple
        index=t5.curselection()[0]
        selected_tuple = t5.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[3])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[4])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[2])
    except IndexError:
        pass

def delete_command():
    backend.delete_entry(selected_tuple[0])

def view_command():
    t5.delete(0,END)
    records = backend.view_all()
    for record in records:
        t5.insert(END,record)

def search_command():
    t5.delete(0,END)
    rows = backend.search_entry(title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get())
    for row in rows:
        t5.insert(END,row)

def add_command():
    backend.add_entry(title_entry.get(),isbn_entry.get(),author_entry.get(),year_entry.get())
    t5.delete(0,END)
    t5.insert(END,(title_entry.get(),isbn_entry.get(),author_entry.get(),year_entry.get()))

def update_command():
    backend.update_entry(selected_tuple[0],title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get())

window = Tk()
window.wm_title("BookStore")

t1 = Label(window,text ="Title" )
t1.grid(row=0,column=0)

title_entry = StringVar()
e1 = Entry(window,textvariable = title_entry)
e1.grid(row=0,column=1)

t2 = Label(window,text ="Author" )
t2.grid(row=0,column=2)

author_entry = StringVar()
e2 = Entry(window,textvariable = author_entry)
e2.grid(row=0,column=3)


t3 = Label(window,text ="Year" )
t3.grid(row=1,column=0)

year_entry = StringVar()
e3 = Entry(window,textvariable = year_entry)
e3.grid(row=1,column=1)

t4 = Label(window,text ="ISBN" )
t4.grid(row=1,column=2)

isbn_entry = StringVar()
e4 = Entry(window,textvariable = isbn_entry)
e4.grid(row=1,column=3)

b1 = Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4 = Button(window,text="Update Selected",width=12,command=update_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

t5 = Listbox(window,height=8,width=35)
t5.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1= Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

t5.configure(yscrollcommand=sb1.set)
sb1.configure(command=t5.yview)

t5.bind('<<ListboxSelect>>',get_selected_record)

window.mainloop()

from tkinter import *
import BackEnd
Window = Tk()
Window.title("by azar")
#this project is created for make master's job easier
#from amirmohammad miralinezhad
#-------------------------Labels--------------------
l1 = Label(Window, text="نام :")
l1.grid(row=0, column=0)

l2 = Label(Window, text="نام خانوادگی :")
l2.grid(row=0, column=2)

l3 = Label(Window, text="شماره دانشجویی :")
l3.grid(row=1, column=0)

l4 = Label(Window, text="تایم کلاس :")
l4.grid(row=1, column=2)

l5 = Label(Window, text="تعداد غیبت :")
l5.grid(row=2, column=0)

Window.resizable(False, False)
#-------------------------Entries--------------------
title_text = StringVar()
e1 = Entry(Window,textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(Window,textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(Window,textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(Window,textvariable=isbn_text)
e4.grid(row=1, column=3)

gheybat_text = StringVar()
e5 = Entry(Window,textvariable=gheybat_text)
e5.grid(row=2, column=1)

list1 = Listbox(Window, width=40 , height=7)
list1.grid(row=3, column=0  , rowspan=6, columnspan=2)

sb1 = Scrollbar(Window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)



def get_selected_row(event):
    global selected_book


    ########
    if len(list1.curselection()) > 0:
        index = list1.curselection()[0]
        selected_book = list1.get(index)
        # title
        e1.delete(0, END)
        e1.insert(END, selected_book[1])
        # author
        e2.delete(0, END)
        e2.insert(END, selected_book[2])
        # year
        e3.delete(0, END)
        e3.insert(END, selected_book[3])
        # isbn
        e4.delete(0, END)
        e4.insert(END, selected_book[4])
        #
        e5.delete( 0, END )
        e5.insert( END, selected_book[5] )

list1.bind("<<ListboxSelect>>", get_selected_row)

#-----------------command--------------------
def clear_list():
    list1.delete( 0, END )

def fill_list(books):
    for book in books:
        list1.insert(END,book)


def view_command():
    clear_list()
    books = BackEnd.view()
    fill_list(books)


def search_command():
    clear_list()
    books = BackEnd.search( title_text.get(), author_text.get(), year_text.get(), isbn_text.get(), gheybat_text.get() )
    fill_list(books)


def add_command():
    BackEnd.insert( title_text.get(), author_text.get(), year_text.get(), isbn_text.get(), gheybat_text.get() )
    view_command()

def delete_command():
    BackEnd.delete( selected_book[0] )
    view_command()

def update_command():
    BackEnd.update(selected_book[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get(), gheybat_text.get())
    view_command()

#------------------Button-----------

b1 = Button(Window,text= "View All", width=12, command=lambda: view_command())
b1.grid(row=2, column=3)
b2 = Button(Window,text= "Search STU", width=12, command=search_command)
b2.grid(row=3, column=3)
b3 = Button(Window,text= "Add STU", width=12, command=add_command)
b3.grid(row=4, column=3)
b4 = Button(Window,text= "Update selected", width=12, command=update_command)
b4.grid(row=5, column=3)
b5 = Button(Window,text= "Delete Selected", width=12, command=delete_command)
b5.grid(row=6, column=3)
b6 = Button(Window,text= "Close", width=12,command=Window.destroy)
b6.grid(row=7, column=3)


view_command()


Window.mainloop()

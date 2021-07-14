import tkinter
# Back_end python file
import back_end

window=tkinter.Tk()
window.title("Book Store")
window.resizable(False, False)

e_id=tkinter.IntVar()

#============================functions============================
# Id of the selected row/book
def get_id(event):
    try:
        global e_id
        row=list.curselection()[0]
        book=list.get(row)
        e_id=book[0]
    
        # Update the text boxes of window using id
        title.delete(0,tkinter.END)
        title.insert(tkinter.END,book[1])

        author.delete(0,tkinter.END)
        author.insert(tkinter.END,book[2])

        year.delete(0,tkinter.END)
        year.insert(tkinter.END,book[3])

        isbn.delete(0,tkinter.END)
        isbn.insert(tkinter.END,book[4])
    except IndexError:
        pass


def view_command():
    list.delete(0,tkinter.END)
    for book in back_end.view():
        list.insert(tkinter.END,book)


def search_command():
    list.delete(0,tkinter.END)
    for book in back_end.search(e_title.get(),e_author.get(),e_year.get(),e_isbn.get()):
        list.insert(tkinter.END,book)

def insert_command():
    back_end.insert(e_title.get(),e_author.get(),e_year.get(),e_isbn.get())
    list.delete(0,tkinter.END)
    list.insert(tkinter.END,(e_title.get(),e_author.get(),e_year.get(),e_isbn.get()))
    
def delete_command():
    back_end.delete(e_id)
    view_command()

def update_command():
    back_end.update(e_id,e_title.get(),e_author.get(),e_year.get(),e_isbn.get())
    view_command()

def clear_command():
    title.delete(0,tkinter.END)
    author.delete(0,tkinter.END)
    year.delete(0,tkinter.END)
    isbn.delete(0,tkinter.END)
    list.delete(0,tkinter.END)


#-----------------------------Row 0-----------------------------
l_title=tkinter.Label(window,text="Tiltle")
l_title.grid(row=0,column=0)

l_author=tkinter.Label(window,text="Author")
l_author.grid(row=0,column=2)

e_title=tkinter.StringVar()
e_author=tkinter.StringVar()

title=tkinter.Entry(window,textvariable=e_title)
title.grid(row=0,column=1)

author=tkinter.Entry(window,textvariable=e_author)
author.grid(row=0,column=3)

#-----------------------------Row 1-----------------------------
l_year=tkinter.Label(window,text="Year")
l_year.grid(row=1,column=0)

l_isbn=tkinter.Label(window,text="ISBN")
l_isbn.grid(row=1,column=2)

e_year=tkinter.StringVar()
e_isbn=tkinter.StringVar()

year=tkinter.Entry(window,textvariable=e_year)
year.grid(row=1,column=1)

isbn=tkinter.Entry(window,textvariable=e_isbn)
isbn.grid(row=1,column=3)

#-----------------------------Row 2-----------------------------
list=tkinter.Listbox(window,height=9,width=35)
list.grid(row=2,column=0,rowspan=7,columnspan=2)

scroll=tkinter.Scrollbar(window)
scroll.grid(row=2,column=2,rowspan=6)

list.configure(yscrollcommand=scroll.set)
scroll.configure(command=list.yview)

# A callback function to the '<>' event:  to execute the function when one or more list items are selected.
list.bind('<<ListboxSelect>>',get_id)

b_view=tkinter.Button(window,text="View all",width=12,command=view_command)
b_view.grid(row=2,column=3)
#-----------------------------Row 3-----------------------------
b_search=tkinter.Button(window,text="Search entry",width=12,command=search_command)
b_search.grid(row=3,column=3)
#-----------------------------Row 4-----------------------------
b_add=tkinter.Button(window,text="Add entry",width=12,command=insert_command)
b_add.grid(row=4,column=3)
#-----------------------------Row 5-----------------------------
b_update=tkinter.Button(window,text="Update",width=12,command=update_command)
b_update.grid(row=5,column=3)
#-----------------------------Row 6-----------------------------
b_delete=tkinter.Button(window,text="Delete",width=12,command=delete_command)
b_delete.grid(row=6,column=3)
#-----------------------------Row 7-----------------------------
b_clear=tkinter.Button(window,text="Clear",width=12,command=clear_command)
b_clear.grid(row=7,column=3)
#-----------------------------Row 8-----------------------------
b_close=tkinter.Button(window,text="Close",width=12,command=window.destroy)
b_close.grid(row=8,column=3)

window.mainloop()

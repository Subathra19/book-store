import sqlite3

def connect():
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    #Querry
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    con.commit()
    con.close()


def insert(title,author,year,isbn):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    #Querry
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    con.commit()
    con.close()

def view():
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM book")
    data=cur.fetchall()
    con.commit()
    con.close()    
    return data

def search(title="",author="",year="",isbn=""):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM book WHERE title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
    data=cur.fetchall()
    con.commit()
    con.close()    
    return data

def update(id,title,author,year,isbn):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    con.commit()
    con.close()  

def delete(id):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    data=cur.fetchall()
    con.commit()
    con.close()       

connect()

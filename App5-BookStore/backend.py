import sqlite3

def create():
    conn = sqlite3.connect("bookstore.db")
    cur  = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookstore(id INTEGER PRIMARY KEY,title TEXT,ISBN INTEGER,author TEXT,year INTEGER)")
    conn.commit()
    conn.close()


def view_all():
    conn = sqlite3.connect("bookstore.db")
    cur  = conn.cursor()
    cur.execute("SELECT * FROM bookstore")
    records = cur.fetchall()
    conn.close()
    return records


def add_entry(title,ISBN,author,year):
    conn = sqlite3.connect("bookstore.db")
    cur  = conn.cursor()
    cur.execute("INSERT INTO bookstore VALUES(NULL,?,?,?,?)",(title,ISBN,author,year))
    conn.commit()
    conn.close()

def search_entry(title="",author="",year="",isbn=""):
     conn = sqlite3.connect("bookstore.db")
     cur  = conn.cursor()
     cur.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR ISBN=?",(title,author,year,isbn))
     rows = cur.fetchall()
     conn.close()
     return rows

def delete_entry(id):
    conn = sqlite3.connect("bookstore.db")
    cur  = conn.cursor()
    cur.execute("DELETE FROM bookstore WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update_entry(id,title,author,year,isbn):
    conn = sqlite3.connect("bookstore.db")
    cur  = conn.cursor()
    cur.execute("UPDATE bookstore SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()


# create()
add_entry("The Sun",468148647,"John Smith",1920)
# delete_entry(2)
# update_entry(4,"adventures",65415465,'SS',1980)
# print(view_all())
# print(search_entry(author="John Smith"))

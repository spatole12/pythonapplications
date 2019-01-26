import sqlite3

class Database:
    # Constructor in other lang
    # the object :'database' created in the frontend.py is passed as argument:"self" in init
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur  = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS bookstore(id INTEGER PRIMARY KEY,title TEXT,ISBN INTEGER,author TEXT,year INTEGER)")
        self.conn.commit()



    def view_all(self):
        self.cur.execute("SELECT * FROM bookstore")
        records = self.cur.fetchall()
        return records


    def add_entry(self,title,ISBN,author,year):
        self.cur.execute("INSERT INTO bookstore VALUES(NULL,?,?,?,?)",(title,ISBN,author,year))
        self.conn.commit()

    def search_entry(self,title="",author="",year="",isbn=""):
         self.cur.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR ISBN=?",(title,author,year,isbn))
         rows = self.cur.fetchall()
         return rows

    def delete_entry(self,id):
        self.cur.execute("DELETE FROM bookstore WHERE id=?",(id,))
        self.conn.commit()

    def update_entry(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE bookstore SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()

    # destructor
    def __del__(self):
        self.conn.close()

# create()
# add_entry("The Sun",468148647,"John Smith",1920)
# delete_entry(2)
# update_entry(4,"adventures",65415465,'SS',1980)
# print(view_all())
# print(search_entry(author="John Smith"))

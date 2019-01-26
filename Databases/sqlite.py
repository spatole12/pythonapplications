# sqlite3
# psycopg2. . . postgres
import sqlite3

def create_table():
    # Establish  a connection
    conn = sqlite3.connect("lite.db")
    # Point a cursor
    cur = conn.cursor()
    # Execute a query
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT,quantity INTEGER, price REAL)")
    # REAL=float
    # Commit connection
    conn.commit()
    # close connection
    conn.close()

def insert(item,quantity,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,price,quantity))
    conn.commit()
    conn.close()


# insert('Sugar',5,3.4)
# insert('Coffee',8,9.2)

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item =?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?,price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()

# delete("Wine Glass")
update(13.5,9,"Coffee")
print(view())

# psycopg2
# psycopg2. . . postgres
import psycopg2

def create_table():
    # Establish  a connection
    conn = psycopg2.connect("dbname='pythondb' user='postgres' password='shivani@123' host='localhost' port='5432'")
    # Point a cursor
    cur = conn.cursor()
    # Execute a query
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT,quantity INTEGER, price REAL)")
    # REAL=float
    # Commit connection
    conn.commit()
    # close connection
    conn.close()

# create_table()

def insert(item,quantity,price):
    conn = psycopg2.connect("dbname='pythondb' user='postgres' password='shivani@123' host='localhost' port='5432'")
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES('%s','%d','%d')" % (item,price,quantity))
    # to avoid sql injection use the below
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,price,quantity))
    conn.commit()
    conn.close()


# insert('Sugar',5,3.4)
# insert('Coffee',8,9.2)

def view():
    conn = psycopg2.connect("dbname='pythondb' user='postgres' password='shivani@123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

# print(view())

def delete(item):
    conn = psycopg2.connect("dbname='pythondb' user='postgres' password='shivani@123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item =%s",(item,))
    conn.commit()
    conn.close()

delete("Sugar")
def update(quantity,price,item):
    conn = psycopg2.connect("dbname='pythondb' user='postgres' password='shivani@123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s,price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

update(13.5,9,"Coffee")
# print(view())

import sqlite3
def create_db ():
    with open ("database.sql","r") as db:
        sql = db.read()

    with sqlite3.connect("tasks.db") as con:
        cur = con.cursor()
        cur.executescript(sql)

if __name__ == "__main__":
    create_db()

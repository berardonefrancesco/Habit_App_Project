import sqlite3

def get_db(name='main.db'):
    db = sqlite3.connect(name)
    create_tables(db)
    return db

def create_tables(db):
    cur = db.cursor()

    cur.execute("""CREATE TABLE if NOT EXISTS habit (
        name TEXT PRIMARY KEY,
        description TEXT)""")

    cur.execute("""CREATE TABLE if NOT EXISTS tracker (
        date TEXT,
        habitName TEXT,
        FOREIGN KEY (habitName) REFERENCES habit(name))""")

    db.commit()

def add_habit(db, name, description):
    cur = db.cursor()
    cur.execute("INSERT INTO habit VALUES (?, ?)", (name, periodicity))
    db.commit()

def complete_habit(db, name, completion_date=None):
    cur = db.cursor()
    if not completion_date:
        from datetime import date
        completion_date=str(date.today())
    cur.execute("INSERT INTO tracker VALUES (?, ?)", (completion_date, name))
    db.commit()

def get_habit_data(db, name):
    cur = db.cursor()
    cur.execute("SELECT * FROM tracker WHERE habitName=?", (name,))
    return cur.fetchall()

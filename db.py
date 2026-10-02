import sqlite3
from datetime import datetime

def get_db(name='main.db'):
    db = sqlite3.connect(name)
    create_tables(db)
    return db

def create_tables(db):
    cur = db.cursor()

    cur.execute("""CREATE TABLE if NOT EXISTS habit (
        name TEXT PRIMARY KEY,
        periodicity TEXT)""")

    cur.execute("""CREATE TABLE if NOT EXISTS tracker (
        date TEXT,
        habitName TEXT,
        FOREIGN KEY (habitName) REFERENCES habit(name))""")

    db.commit()

def add_habit(db, name, periodicity):
    cur = db.cursor()
    cur.execute("INSERT INTO habit VALUES (?, ?)", (name, periodicity))
    db.commit()

def complete_habit(db, name, completion_date=None):
    cur = db.cursor()
    if not completion_date:
            completion_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("INSERT INTO tracker VALUES (?, ?)", (completion_date, name))
    db.commit()

def get_habit_data(db, name):
    cur = db.cursor()
    cur.execute("SELECT * FROM tracker WHERE habitName=?", (name,))
    return cur.fetchall()

def get_specific_periodicity(db, periodicity):
    cur = db.cursor()
    cur.execute("SELECT * FROM habit WHERE periodicity=?", (periodicity,))
    return cur.fetchall()

def get_tracker_data(db):
    cur = db.cursor()
    cur.execute("SELECT * FROM habit")
    retun cur.fetchall()
import sqlite3
from datetime import datetime, timedelta

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
    return cur.fetchall()

from datetime import datetime, timedelta

def calculate_max_streak(db):
    cur = db.cursor()
    cur.execute("SELECT habitName, date FROM tracker")
    data = cur.fetchall()

    habits = {}

    #Grouping date per habit
    for habit_name, date_string in data:
        date = datetime.strptime(
            date_string,
            "%Y-%m-%d %H:%M:%S"
        ).date()

        if habit_name not in habits:
            habits[habit_name] = []

        habits[habit_name].append(date)

    max_streak = 0

    #Calculate max streak
    for dates in habits.values():
        dates = sorted(set(dates))
        current_streak = 1
        for i in range(1, len(dates)):
            if dates[i] == dates[i - 1] + timedelta(days=1):
                current_streak += 1
            else:
                current_streak = 1
            max_streak = max(max_streak, current_streak)
    return max_streak

from datetime import datetime, timedelta


def calculate_habit_streak(db, name):
    data = get_habit_data(db, name)
    dates = []
    for habit_name, date_string in data:
        date = datetime.strptime(
            date_string,
            "%Y-%m-%d %H:%M:%S"
        ).date()
        dates.append(date)
    dates = sorted(set(dates))
    if not dates:
        return 0
    max_streak = 1
    current_streak = 1
    for i in range(1, len(dates)):
        if dates[i] == dates[i - 1] + timedelta(days=1):
            current_streak += 1
        else:
            current_streak = 1
        max_streak = max(max_streak, current_streak)
    return max_streak
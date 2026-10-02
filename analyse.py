from db import get_habit_data

def calculate_habit_len(db, habit):
    """Calculate the len of the habit.

    :param db: an initialized sqlite3 database connection
    :param habit: name of the habit present in the db
    :return: lenght of habit completion events
    """
    data = get_habit_data(db, habit)
    return len(data)

def habit_same_periodicity(db, periodicity):
    data = get_habit_periodicity(db, periodicity)
    return data

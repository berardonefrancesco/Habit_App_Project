from db import add_habit, complete_habit
from datetime import datetime

#add docstring for all the def

class Habit:

  def __init__(self, name, periodicity, creation_date: str = None):
    self.name = name
    self.periodicity = periodicity
    if not creation_date:
      creation_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.creation_date = creation_date
    self.completed_date = []

  def reset(self):
    self.completed_date = []

  def complete(self):
    self.completed_date.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

  def __str__(self):
    return f"{self.name}: {self.completed_date}"

  def store(self, db):
    add_habit(db, self.name, self.periodicity)

  def add_event(self, db, date = None):
    complete_habit(db, self.name, self.completed_date)
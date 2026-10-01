from db import add_habit, complete_habit
 
#add docstring for all the def

class Habit:

  def __init__(self, name, periodicity):
    self.name = name
    self.periodicity = periodicity
    self.completed_date = []

  def reset(self):
    self.completed_date = []

  def __str__(self):
    return f"{self.name}: {self.completed_date}"

  def store(self, db):
    add_habit(db, self.name, self.periodicity)

  def add_event(self, db, date: str = None):
    complete_habit(db, self.name, date)
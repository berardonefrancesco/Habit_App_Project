Class Habit:

  dif __init__(self, name, periodicity):
    self.name = name
    self.periodicity = periodicity
    self.completed_date = []

  dif complete(self, date):
    self.completed_date.append(date)

Leggere = Habit("Leggere","Daily")
Leggere.complete("2026-09-30")
print(Leggere.name)
print(Leggere.periodicity)
print(Leggere.completed_date)
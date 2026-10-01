from habit import Habit

class testHabit:

    def test_Habit(self):
        habit = Habit("test_habit_1", "test_periodicity_1")
        habit.complete_habit()
        habit.reset()
        habit.complete_habit()

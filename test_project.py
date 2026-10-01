from habit import Habit, db_Habit
from db import get_db, add_habit, complete_habit, get_habit_data
from analyse import calculate_habit_len

class test_Habit:

    def setup_method(self):
        self.db = get_db("test.db")
        add_habit(self.db, "test_habit", "test_periodicity")
        #Here you can add test data
        complete_habit(self.db, "test_habit", "2026-09-27")
        complete_habit(self.db, "test_habit", "2026-09-28")
        complete_habit(self.db, "test_habit", "2026-09-30")
        complete_habit(self.db, "test_habit", "2026-10-01")

    def test_Habit(self):
        habit = Habit("test_habit_1", "test_periodicity_1")
        habit.store(self.db)
        habir.add_habit(self.db)
        habit.complete_habit()
        habit.reset()
        habit.complete_habit()

    def teardown_method(self):
        import os
        os.remove("test.db")

    def test_db_habit(self):
        data = get_habit_data(self.db, "test_habit")
        assert len(data) == 4

        count = calculate_habit_len(self.db, "test_habit")
        assert count == 4
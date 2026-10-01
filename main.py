import questionary
from db import get_db
from habit import Habit
from analyse import calculate_habit_len

def cli():
    db = get_db()
    questionary.confirm("Are you ready?").ask()

    stop = False

    while not stop:
        choice.questionary.select(
            choices=["Create","Complete Habit","Analyse","Exit"]
        ).ask()

        name = questionary.text("What's the name of your habit?").ask()

        if choice == "Create":
            periodicity = questionary.text("What's the periodicity of your habit?").ask()
            habit = Habit(name, periodicity)
            habit.store(db)
        elif choice == "Complete Habit":
            periodicity = questionary.text("What's the periodicity of your habit?").ask()
            habit = Habit(name, periodicity)
            habit.add_event(db)
        elif choice == "Analyse":
            lenght = calculate_habit_len(db, name)
            #Qui devo aggiungere qualcosa sullo strike come print
        else:
            print("Bye")
            stop = True

    cli()
import questionary
from db import get_db
from habit import Habit
from analyse import calculate_habit_len

def cli():
    db = get_db()
    questionary.confirm("Are you ready?").ask()

    stop = False

    while not stop:
        choice = questionary.select(
            "What do you want to do?",
            choices=["Create","Complete Habit","Analyse","Exit"]
        ).ask()
        if choice == "Exit":
            pass
        else:
            name = questionary.text("What's the name of your habit?").ask()

        if choice == "Create":
            periodicity = questionary.select(
                "What's the periodicity of your habit?",
                choices=["Daily","Weekly"]
            ).ask()
            habit = Habit(name, periodicity)
            habit.store(db)
        elif choice == "Complete Habit":
            periodicity = questionary.select(
                "What's the periodicity of your habit?",
                choices=["Daily","Weekly"]
            ).ask()
            habit = Habit(name, periodicity)
            habit.add_event(db)
        elif choice == "Analyse":
            lenght = calculate_habit_len(db, name)
            print(lenght)
            #Qui devo aggiungere qualcosa sullo strike come print
        else:
            print("Bye")
            stop = True

if __name__ == '__main__':
    cli()
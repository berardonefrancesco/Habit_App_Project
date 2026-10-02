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
            choices=["Create","Check Habit","Analyse","Exit"]
        ).ask()
        if choice == "Exit":
            pass
        else:
            name = questionary.text("Which habit do you want to track?").ask()

        if choice == "Create":
            name = questionary.text("Which habit do you want to track?").ask()
            periodicity = questionary.select(
                "How often do you want to check-off your habit?",
                choices=["Daily","Weekly"]
            ).ask()
            habit = Habit(name, periodicity)
            habit.store(db)
        elif choice == "Complete Habit":
            name = questionary.text("Great job! Which habit did you build today?").ask()
            #periodicity = questionary.select(
                #"What's the periodicity of your habit?",
                #choices=["Daily","Weekly"]
            #).ask()
            #habit = Habit(name, periodicity)
            #habit.add_event(db)
            #Qui deve fare il completamento dell'abitudine
        elif choice == "Analyse":
            analysis_choice = questionary.select(
                "What do you want to know today?",
                choices=[
                    "Return a list of all currently tracked habits",
                    "Return a list of all habits with the same periodicity",
                    "Return the longest run streak of all defined habits",
                    "Return the longest run streak for a given habit"
                    ]
            ).ask()
            
            lenght = calculate_habit_len(db, name)
            print(lenght)
            #Qui devo aggiungere qualcosa sullo strike come print
        else:
            print("Bye")
            stop = True

if __name__ == '__main__':
    cli()
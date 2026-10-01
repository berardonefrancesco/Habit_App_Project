import questionary
from db import get_db
from habit import Habit

def cli():
    db = get_db()
    questionary.confirm("Are you ready?").ask()
    choice.questionary.select(
        choices=["Create","Incremenet","Analyse","Exit"]
    ).ask()

    if choice == "Create":
        name = questionary.text("What's the name of your habit?").ask()
        periodicity = questionary.text("What's the periodicity of your habit?").ask()
        habit = Habit(name, periodicity)
        habit.store(db)

if __name__ == '__main__':
    cli()
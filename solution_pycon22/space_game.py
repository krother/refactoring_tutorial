"""
Space Travel Game

A simple text adventure written for a refactoring tutorial.

github.com/krother/refactoring_tutorial

pytest test_space_game.py

1. select a code section
2. name the function
3. indent the code
4. make a parameter out of every variable
   not created inside the function
5. Add a return statement
6. Add a function call
7. Run the tests
"""
from text_en import TEXT

#TODO: use an Enum
credits, engines, copilot, game_end = range(4)


def display_inventory(flags):
    print("-" * 79)
    inventory = "\nYou have: "
    inventory += "plenty of credits, " if credits in flags else ""
    inventory += "a hyperdrive, " if engines in flags else ""
    inventory += "a skilled copilot, " if copilot in flags else ""
    if inventory.endswith(", "):
        print(inventory.strip(", "))


def select_planet(destinations):
    print("\nWhere do you want to travel?")
    for i, d in enumerate(destinations, 1):
        print(f"[{i}] {d}")

    choice = input()
    return destinations[int(choice) - 1]


def engine_puzzle(flags):
    if engines not in flags:
        print(TEXT["HYPERDRIVE_SHOPPING_QUESTION"])
        if input() == "yes":
            if credits in flags:
                flags.add(engines)
            else:
                print(TEXT["HYPERDRIVE_TOO_EXPENSIVE"])

def quiz(flags):
    if credits not in flags:
        print(TEXT["SIRIUS_QUIZ_QUESTION"])
        answer = input()
        if answer == "2":
            print(TEXT["SIRIUS_QUIZ_CORRECT"])
            flags.add(credits)
        else:
            print(TEXT["SIRIUS_QUIZ_INCORRECT"])

def jump_into(flags):
    if input() == "yes":
        if engines in flags and copilot in flags:
            print(TEXT["BLACK_HOLE_COPILOT_SAVES_YOU"])
        else:
            print(TEXT["BLACK_HOLE_CRUNCHED"])
        flags.add(game_end)


def hire_copilot(flags):
    if copilot not in flags:
        print(TEXT["ORION_HIRE_COPILOT_QUESTION"])
        if input() == "42":
            print(TEXT["COPILOT_QUESTION_CORRECT"])
            flags.add(copilot)
        else:
            print(TEXT["COPILOT_QUESTION_INCORRECT"])


def do_nothing(flags):
    pass


class Planet:

    def __init__(self, name, destinations, puzzle=do_nothing):
        self.name = name
        self.description = TEXT[name.upper() + '_DESCRIPTION']
        self.destinations = destinations
        self.puzzle = puzzle

    def visit(self, flags):
        """interaction with planets"""
        print(self.description)
        self.puzzle(flags)

PLANETS = {
    p.name: p for p in [
    Planet('earth', ["centauri", "sirius"]),
    Planet('sirius', ["orion", "earth", "black_hole"], quiz),
    Planet('orion', ["centauri", "sirius"], hire_copilot),
    Planet('centauri', ["earth", "orion"], engine_puzzle),
    Planet('black_hole', ["sirius"], jump_into)
    ]
}

def travel():
    print(TEXT["OPENING_MESSAGE"])

    planet = PLANETS["earth"]
    flags = set()

    while game_end not in flags:
        display_inventory(flags)
        planet.visit(flags)
        if game_end not in flags:
            planet = PLANETS[select_planet(planet.destinations)]

    print(TEXT["END_CREDITS"])


if __name__ == "__main__":
    travel()

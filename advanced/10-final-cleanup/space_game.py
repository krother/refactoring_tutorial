"""
Space Travel Game

A simple text adventure written for a refactoring tutorial.
"""
from text_en import TEXT


#
# Puzzle functions
#
def buy_engine(flags):
    if not 'engines' in flags:
        print(TEXT["HYPERDRIVE_SHOPPING_QUESTION"])
        if input() == "yes":
            if 'credits' in flags:
                print(TEXT["HYPERDRIVE_SHOPPING_SUCCESS"])
                flags.add('engines')
            else:
                print(TEXT["HYPERDRIVE_TOO_EXPENSIVE"])


def quiz_show(flags):
    if not 'credits' in flags:
        print(TEXT["SIRIUS_QUIZ_QUESTION"])
        answer = input()
        if answer == "2":
            print(TEXT["SIRIUS_QUIZ_CORRECT"])
            flags.add('credits')
        else:
            print(TEXT["SIRIUS_QUIZ_INCORRECT"])


def hire_copilot(flags):
    if 'engines' in flags and not 'copilot' in flags:
        print(TEXT["ORION_HIRE_COPILOT_QUESTION"])
        if input() == "yes":
            flags.add('copilot')
    else:
        print(TEXT["ORION_NOTHING_GOING_ON"])


def examine_black_hole(flags):
    if input(TEXT["BLACK_HOLE_EXAMINE_QUESTION"]) == "yes":
        if 'engines' in flags and 'copilot' in flags:
            print(TEXT["BLACK_HOLE_COPILOT_SAVES_YOU"])

            print(TEXT["ORACLE_QUESTION"])
            answer = input()
            if answer == "42":
                print(TEXT["ORACLE_CORRECT"])
                flags.add('game_end')
                print(TEXT["END_CREDITS"])  # skips last move 
            else:
                print(TEXT["ORACLE_INCORRECT"])
                flags.remove('engines')
        else:
            print(TEXT["BLACK_HOLE_CRUNCHED"])
            flags.add('game_end')


class Planet:

    def __init__(self, name, destinations, puzzle=None):
        self.name = name
        self.description = TEXT[name.upper() + '_DESCRIPTION']
        self.destinations = destinations
        self.puzzle = puzzle

    def visit(self, flags):
        print(self.description)
        if self.puzzle:
            self.puzzle(flags)

    def display_destinations(self):
        print("\nWhere do you want to travel?")
        position = 1
        for d in self.destinations:
            print(f"[{position}] {d}")
            position += 1


PLANETS = {
    'earth': Planet('earth', ['centauri', 'sirius']),
    'sirius': Planet('sirius', ["orion", "earth", "black_hole"],quiz_show),
    'orion': Planet('orion', ["centauri", "sirius"], hire_copilot),
    'centauri': Planet('centauri', ['earth', 'orion'], buy_engine),
    'black_hole': Planet('black_hole', ['sirius'], examine_black_hole)
}


def display_inventory(flags):
    print(TEXT["BAR"])
    if 'credits' in flags:
        print("You have plenty of stellar credits.")
    if 'engines' in flags:
        print("You have a brand new next-gen hyperdrive.")
    if 'copilot' in flags:
        print("A furry tech-savvy copilot is on board.")



def select_planet(destinations):
    # choose the next planet
    travel_to = None
    while travel_to not in destinations:
        text = input()
        try:
            index = int(text)
            travel_to = destinations[index - 1]
        except ValueError:
            print("please enter a number")
        except IndexError:
            print(f"please enter 1-{len(destinations)}")
    return PLANETS[travel_to]



def travel():

    print(TEXT["OPENING_MESSAGE"])
    flags = set()

    planet = PLANETS["earth"]
    planet.visit(flags)

    while not 'game_end' in flags:
        planet.display_destinations()
        planet = select_planet(planet.destinations)
        display_inventory(flags)
        planet.visit(flags)


if __name__ == "__main__":
    travel()

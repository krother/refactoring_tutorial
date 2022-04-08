"""
Space Travel Game

A simple text adventure written for a refactoring tutorial.
"""
from text_en import TEXT


STARMAP = {
    'earth': ['centauri', 'sirius'],
    'centauri': ['earth', 'orion'],
    'sirius': ["orion", "earth", "BH#0997"],
    'orion': ["centauri", "sirius"],
    'BH#0997': ['sirius'],
    'oracle': ['earth']
}


def display_inventory(flags):
    print(TEXT["BAR"])
    if 'credits' in flags:
        print("You have plenty of stellar credits.")
    if 'engines' in flags:
        print("You have a brand new next-gen hyperdrive.")
    if 'copilot' in flags:
        print("A furry tech-savvy copilot is on board.")


def display_destinations(destinations):
    print("\nWhere do you want to travel?")
    position = 1
    for d in destinations:
        print(f"[{position}] {d}")
        position += 1


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
    return travel_to


def visit_planet(planet, flags):

    if planet == "earth":
        print(TEXT["EARTH_DESCRIPTION"])

    if planet == "centauri":
        print(TEXT["CENTAURI_DESCRIPTION"])

        if not 'engines' in flags:
            print(TEXT["HYPERDRIVE_SHOPPING_QUESTION"])
            if input() == "yes":
                if 'credits' in flags:
                    print(TEXT["HYPERDRIVE_SHOPPING_SUCCESS"])
                    flags.add('engines')
                else:
                    print(TEXT["HYPERDRIVE_TOO_EXPENSIVE"])

    if planet == "sirius":
        print(TEXT["SIRIUS_DESCRIPTION"])

        if not 'credits' in flags:
            print(TEXT["SIRIUS_QUIZ_QUESTION"])
            answer = input()
            if answer == "2":
                print(TEXT["SIRIUS_QUIZ_CORRECT"])
                flags.add('credits')
            else:
                print(TEXT["SIRIUS_QUIZ_INCORRECT"])

    if planet == "orion":

        if 'engines' in flags and not 'copilot' in flags:
            print(TEXT["ORION_DESCRIPTION"])
            print(TEXT["ORION_HIRE_COPILOT_QUESTION"])
            if input() == "yes":
                flags.add('copilot')
        else:
            print(TEXT["ORION_DESCRIPTION"])
            print(TEXT["ORION_NOTHING_GOING_ON"])

    if planet == "BH#0997":
        print(TEXT["BLACK_HOLE_DESCRIPTION"])

        if input(TEXT["BLACK_HOLE_EXAMINE_QUESTION"]) == "yes":
            if 'engines' in flags and 'copilot' in flags:
                print(TEXT["BLACK_HOLE_COPILOT_SAVES_YOU"])
                planet = "oracle"
            else:
                print(TEXT["BLACK_HOLE_CRUNCHED"])
                flags.add('dead')

    if planet == "oracle":
        print(TEXT["ORACLE_QUESTION"])
        answer = input()
        if answer == "42":
            print(TEXT["ORACLE_CORRECT"])
            flags.add('crystal_found')
        else:
            print(TEXT["ORACLE_INCORRECT"])
            flags.remove('engines')

    return planet


def travel():

    print(TEXT["OPENING_MESSAGE"])

    planet = "earth"
    flags = set()

    while not ('crystal_found' in flags or 'dead' in flags):

        display_inventory(flags)
        planet = visit_planet(planet, flags)

        if not 'dead' in flags:
            destinations = STARMAP[planet]
            display_destinations(destinations)
            planet = select_planet(destinations)

    print(TEXT["END_CREDITS"])


if __name__ == "__main__":
    travel()

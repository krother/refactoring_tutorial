"""
Space Travel Game

A simple text adventure written for a refactoring tutorial.
"""
from text_en import TEXT


def travel():

    print(TEXT["OPENING_MESSAGE"])

    planet = "earth"
    engines = False
    copilot = False
    credits = False
    crystal_found = False

    while not crystal_found:

        print(TEXT["BAR"])

        # display inventory
        if credits:
            print("You have plenty of stellar credits.")
        if engines:
            print("You have a brand new next-gen hyperdrive.")
        if copilot:
            print("A furry tech-savvy copilot is on board.")

        #
        # interaction with planets
        #
        if planet == "earth":
            destinations = ["centauri", "sirius"]
            print(TEXT["EARTH_DESCRIPTION"])

        if planet == "centauri":
            print(TEXT["CENTAURI_DESCRIPTION"])
            destinations = ["earth", "orion"]

            if not engines:
                print(TEXT["HYPERDRIVE_SHOPPING_QUESTION"])
                if input() == "yes":
                    if credits:
                        print(TEXT["HYPERDRIVE_SHOPPING_SUCCESS"])
                        engines = True
                    else:
                        print(TEXT["HYPERDRIVE_TOO_EXPENSIVE"])

        if planet == "sirius":
            print(TEXT["SIRIUS_DESCRIPTION"])
            destinations = ["orion", "earth", "BH#0997"]

            if not credits:
                print(TEXT["SIRIUS_QUIZ_QUESTION"])
                answer = input()
                if answer == "2":
                    print(TEXT["SIRIUS_QUIZ_CORRECT"])
                    credits = True
                else:
                    print(TEXT["SIRIUS_QUIZ_INCORRECT"])

        if planet == "orion":
            destinations = ["centauri", "sirius"]

            if engines and not copilot:
                print(TEXT["ORION_DESCRIPTION"])
                print(TEXT["ORION_HIRE_COPILOT_QUESTION"])
                if input() == "yes":
                    copilot = True
            else:
                print(TEXT["ORION_DESCRIPTION"])
                print(TEXT["ORION_NOTHING_GOING_ON"])

        if planet == "BH#0997":
            print(TEXT["BLACK_HOLE_DESCRIPTION"])
            destinations = ["sirius"]
            if input(TEXT["BLACK_HOLE_EXAMINE_QUESTION"]) == "yes":
                if engines and copilot:
                    print(TEXT["BLACK_HOLE_COPILOT_SAVES_YOU"])
                    planet = "oracle"
                else:
                    print(TEXT["BLACK_HOLE_CRUNCHED"])
                    return

        if planet == "oracle":
            print(TEXT["ORACLE_QUESTION"])
            answer = input()
            if answer == "42":
                print(TEXT["ORACLE_CORRECT"])
                crystal_found = True
            else:
                print(TEXT["ORACLE_INCORRECT"])
                engines = False

            destinations = ["earth"]

        # display hyperjump destinations
        print("\nWhere do you want to travel?")
        position = 1
        for d in destinations:
            print(f"[{position}] {d}")
            position += 1

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
        planet = travel_to

    print(TEXT["END_CREDITS"])


if __name__ == "__main__":
    travel()

"""
Space Travel Game

A simple text adventure written for a refactoring tutorial.
"""

TEXT = {
    "OPENING_MESSAGE": """
*********************************************************************

    You and your trusted spaceship set out to look for 
    fame, wisdom, and adventure.
    The stars are waiting for you.

""",
    "BAR": "\n*********************************************************************\n",
    "EARTH_DESCRIPTION": "\nYou are on Earth. The cradle of humankind. A rather dull place.",
    "CENTAURI_DESCRIPTION": "\nYou are on Alpha Centauri. A buzzing trade hub.\nYou can buy almost anything here.",
    "HYPERDRIVE_SHOPPING_QUESTION": """
They have a brand new next-generation hyperdrive with a built-in GPU.
    
Would you like to buy one [yes/no]""",
    "HYPERDRIVE_TOO_EXPENSIVE": """
You cannot afford it. The GPU is too expensive.""",
    "HYPERDRIVE_SHOPPING_SUCCESS": """
Your spaceship now has a shiny hyperdrive on both sides.
""",
    "SIRIUS_DESCRIPTION": """
You are on Sirius. The system is full of media companies
and content delivery networks.
""",
    "SIRIUS_QUIZ_QUESTION": """
You manage to get a place in *Stellar* - the greatest quiz show in the universe.
And here is your question:

Which star do you find on the shoulder of Orion?

[1] Altair
[2] Betelgeuse
[3] Aldebaran
[4] Andromeda
""",
    "SIRIUS_QUIZ_CORRECT": """
*Correct!!!* You win a ton or credits.
""",
    "SIRIUS_QUIZ_INCORRECT": """
Sorry, this was the wrong answer. Don't take it too sirius.
Better luck next time.
""",
    "ORION_DESCRIPTION": """
You are on Orion. An icy world inhabited by monosyllabic furry sentients.
""",
    "ORION_HIRE_COPILOT_QUESTION": """
You approach the natives at the spaceport
One of them points at your hyperdrive and says 'Nice!'

Do you want to hire them as a copilot? [yes/no]
""",
    "ORION_NOTHING_GOING_ON": """
They are not very talkative.
""",
    "BLACK_HOLE_DESCRIPTION": """
You are close to Black Hole #0997. Maybe coming here was a really stupid idea.
""",
    "BLACK_HOLE_EXAMINE_QUESTION": """
Do you want to examine the black hole closer? [yes/no]
""",
    "BLACK_HOLE_CRUNCHED": """
The black hole condenses your spaceship into a grain of dust.

    THE END
""",
    "BLACK_HOLE_COPILOT_SAVES_YOU": """
On the rim of the black hole your copilot blurts out:

    Turn left!

You ignite the next-gen hyperdrive, creating a time-space anomaly.
You travel through an orthogonal dimension where you experience wonders beyond description.
""",
    "END_CREDITS": """
You return from your adventure wise and with good stories to tell.

    THE END
""",
}


def travel():

    print(TEXT["OPENING_MESSAGE"])

    planet = "earth"
    engines = False
    copilot = False
    credits = False
    game_end = False

    while not game_end:

        print(TEXT["BAR"])

        # display inventory
        if credits:
            print("You have plenty of credits.")
        if engines:
            print("You have a brand new hyperdrive.")
        if copilot:
            print("A tech-savvy copilot is on board.")

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
                    game_end = True
                else:
                    print(TEXT["BLACK_HOLE_CRUNCHED"])
                    return

        if not game_end:
            # select next planet
            print("\nWhere do you want to travel?")
            position = 1
            for d in destinations:
                print(f"[{position}] {d}")
                position += 1

            choice = input()
            planet = destinations[int(choice) - 1]

    print(TEXT["END_CREDITS"])


if __name__ == "__main__":
    travel()

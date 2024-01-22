"""
Space Travel Game

A simple text adventure written for a refactoring tutorial.
"""
from text_en import TEXT
from typing import Literal, Callable
from pydantic import BaseModel


Flag = Literal["engines", "credits", "copilot", "game_end"]

# oldschool
# ENGINES, CREDITS, COPILOT, GAME_END = range(4)


def display_inventory(flags: set[Flag]) -> None:
    print("-" * 79)
    inventory = "\nYou have: "
    inventory += "plenty of credits, " if "credits" in flags else ""
    inventory += "a hyperdrive, " if "engines" in flags else ""
    inventory += "a skilled copilot, " if "copilot" in flags else ""
    if inventory.endswith(", "):
        print(inventory.strip(", "))


def select_planet(destinations: list[str]) -> str:
    print("\nWhere do you want to travel?")
    position = 1
    for d in destinations:
        print(f"[{position}] {d}")
        position += 1
    choice = input()
    return destinations[int(choice) - 1]



def buy_hyperdrive(flags):
    if not "engines" in flags:
        print(TEXT["HYPERDRIVE_SHOPPING_QUESTION"])
        if input() == "yes":
            if "credits" in flags:
                flags.add("engines")
            else:
                print(TEXT["HYPERDRIVE_TOO_EXPENSIVE"])


def quiz_show(flags):
    if not "credits" in flags:
        print(TEXT["SIRIUS_QUIZ_QUESTION"])
        answer = input()
        if answer == "2":
            print(TEXT["SIRIUS_QUIZ_CORRECT"])
            flags.add("credits")
        else:
            print(TEXT["SIRIUS_QUIZ_INCORRECT"])


def hire_copilot(flags):
    if not "copilot" in flags:
        print(TEXT["ORION_HIRE_COPILOT_QUESTION"])
        if input() == "42":
            print(TEXT["COPILOT_QUESTION_CORRECT"])
            flags.add("copilot")
        else:
            print(TEXT["COPILOT_QUESTION_INCORRECT"])


def navigate_black_hole(flags):
    if input() == "yes":
        flags.add("game_end")
        if "engines" in flags and "copilot" in flags:
            print(TEXT["BLACK_HOLE_COPILOT_SAVES_YOU"])
        else:
            print(TEXT["BLACK_HOLE_CRUNCHED"])


class Planet(BaseModel):
    name: str
    description: str
    connections: list[str]
    puzzle_function: Callable = None

    def visit(self, flags: set[Flag]):
        print(self.description)
        if self.puzzle_function:
            self.puzzle_function(flags)


Planets = {
    "earth": Planet(
        name = "earth",
        description = TEXT["EARTH_DESCRIPTION"],
        connections = ["centauri", "sirius"],
    ),
    "centauri": Planet(
        name = "centauri",
        description = TEXT["CENTAURI_DESCRIPTION"],
        connections = ["earth", "orion"],
        puzzle_function = buy_hyperdrive,
    ),
    "sirius": Planet(
        name = "sirius",
        description = TEXT["SIRIUS_DESCRIPTION"],
        connections = ["orion", "earth", "black_hole"],
        puzzle_function = quiz_show,
    ),
    "orion": Planet(
        name = "orion",
        description = TEXT["ORION_DESCRIPTION"],
        connections = ["centauri", "sirius"],
        puzzle_function = hire_copilot,
    ),
    "black_hole": Planet(
        name = "black_hole",
        description = TEXT["BLACK_HOLE_DESCRIPTION"],
        connections=["sirius"],
        puzzle_function = navigate_black_hole
    )
}


def travel() -> None:
    print(TEXT["OPENING_MESSAGE"])

    planet = Planets["earth"]
    flags: set[Flag] = set()

    while not "game_end" in flags:
        display_inventory(flags=flags)
        planet.visit(flags=flags)
        if not "game_end" in flags:
            planet = Planets[select_planet(destinations=planet.connections)]

    print(TEXT["END_CREDITS"])


if __name__ == "__main__":
    travel()

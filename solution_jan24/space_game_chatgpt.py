
from text_en import TEXT


class SpaceTravelGame:
    def __init__(self):
        self.planet = "earth"
        self.engines = False
        self.copilot = False
        self.credits = False
        self.game_end = False

    def display_inventory(self):
        print("-" * 79)
        inventory = "\nYou have: "
        inventory += "plenty of credits, " if self.credits else ""
        inventory += "a hyperdrive, " if self.engines else ""
        inventory += "a skilled copilot, " if self.copilot else ""
        if inventory.endswith(", "):
            print(inventory.strip(", "))

    def interact_with_earth(self):
        destinations = ["centauri", "sirius"]
        print(TEXT["EARTH_DESCRIPTION"])
        return destinations

    def interact_with_centauri(self):
        destinations = ["earth", "orion"]
        print(TEXT["CENTAURI_DESCRIPTION"])
        if not self.engines:
            print(TEXT["HYPERDRIVE_SHOPPING_QUESTION"])
            if input() == "yes" and self.credits:
                self.engines = True
            else:
                print(TEXT["HYPERDRIVE_TOO_EXPENSIVE"])
        return destinations

    def interact_with_sirius(self):
        destinations = ["orion", "earth", "black_hole"]
        print(TEXT["SIRIUS_DESCRIPTION"])
        if not self.credits:
            print(TEXT["SIRIUS_QUIZ_QUESTION"])
            answer = input()
            if answer == "2":
                print(TEXT["SIRIUS_QUIZ_CORRECT"])
                self.credits = True
            else:
                print(TEXT["SIRIUS_QUIZ_INCORRECT"])
        return destinations

    def interact_with_orion(self):
        destinations = ["centauri", "sirius"]
        print(TEXT["ORION_DESCRIPTION"])
        if not self.copilot:
            print(TEXT["ORION_HIRE_COPILOT_QUESTION"])
            if input() == "42":
                print(TEXT["COPILOT_QUESTION_CORRECT"])
                self.copilot = True
        return destinations

    def interact_with_black_hole(self):
        destinations = ["sirius"]
        print(TEXT["BLACK_HOLE_DESCRIPTION"])
        if input() == "yes":
            if self.engines and self.copilot:
                print(TEXT["BLACK_HOLE_COPILOT_SAVES_YOU"])
                self.game_end = True
            else:
                print(TEXT["BLACK_HOLE_CRUNCHED"])
                return destinations

    def select_next_planet(self, destinations):
        print("\nWhere do you want to travel?")
        position = 1
        for d in destinations:
            print(f"[{position}] {d}")
            position += 1

        choice = input()
        self.planet = destinations[int(choice) - 1]

    def play_game(self):
        print(TEXT["OPENING_MESSAGE"])

        while not self.game_end:
            self.display_inventory()

            if self.planet == "earth":
                destinations = self.interact_with_earth()

            elif self.planet == "centauri":
                destinations = self.interact_with_centauri()

            elif self.planet == "sirius":
                destinations = self.interact_with_sirius()

            elif self.planet == "orion":
                destinations = self.interact_with_orion()

            elif self.planet == "black_hole":
                destinations = self.interact_with_black_hole()

            self.select_next_planet(destinations)

        print(TEXT["END_CREDITS"])


if __name__ == "__main__":
    game = SpaceTravelGame()
    game.play_game()

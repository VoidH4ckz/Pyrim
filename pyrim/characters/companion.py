#Pyrim/characters/companion.py

class Companion:
    def __init__(self, name, description, unlock_level):
        self.name = name
        self.description = description
        self.unlock_level = unlock_level
        self.is_unlocked = False

    def unlock(self, player_level):
        if player_level >= self.unlock_level:
            self.is_unlocked = True
            print(f"{self.name} has been unlocked as a companion!")
        else:
            print(f"{self.name} is not yet available as a companion. You need to reach level {self.unlock_level}.")


# Define companion characters
companions_to_unlock = [
    Companion("Lidia", "A loyal friend.", 5),
    Companion("Morpheous", "A mysterious ally.", 10),
    Companion("Savanah", "A powerful warrior.", 15),
    Companion("Freya", "A magical companion.", 20),
    Companion("Samara", "An ancient guardian.", 25),
]
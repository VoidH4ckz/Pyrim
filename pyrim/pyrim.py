import os
import pyfiglet
from colorama import Fore
from menus.explore_menu import explore_menu
from menus.shop_menu import shop_menu
from menus.quest_menu import Quest
from utils import format_text
from characters.player import Player

def allocate_attributes():
    strength = 0
    dexterity = 0
    wisdom = 0
    intelligence = 0
    luck = 0
    remaining_points = 1

    while remaining_points > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + format_text("~~~~~~~~~~~~~~/Allocate Attribute Points:\~~~~~~~~~~~~~~"))
        print(f"Remaining attribute points: {remaining_points}")
        print(f"1. Strength ({strength})")
        print(f"2. Dexterity ({dexterity})")
        print(f"3. Wisdom ({wisdom})")
        print(f"4. Intelligence ({intelligence})")
        print(f"5. Luck ({luck})")

        attribute_choice = input("Choose an attribute to increase (1 - 5): ")

        if attribute_choice == "1":
            strength += 1
        elif attribute_choice == "2":
            dexterity += 1
        elif attribute_choice == "3":
            wisdom += 1
        elif attribute_choice == "4":
            intelligence += 1
        elif attribute_choice == "5":
            luck += 1
        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")
            continue

        remaining_points -= 1

    return strength, dexterity, wisdom, intelligence, luck

def display_character_info(player):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + format_text("~~~~~~~~~~~~~~~/Character Information:\~~~~~~~~~~~~~~~"))
    print(f"Name: {player.name}")
    print(f"Age: {player.age}")
    print(f"Eye Color: {player.eye}")
    print(f"Height: {player.height}")
    print(f"Race: {player.race}")
    print(f"Origin Country: {player.country}")
    print(f"Class: {player.character_class}")
    print(f"Experience: {player.experience}/{100 * player.level}")
    
    print(f"___________________________________________")
    
    print(f"Strength: {player.strength}")
    print(f"Dexterity: {player.dexterity}")
    print(f"Wisdom: {player.wisdom}")
    print(f"Intelligence: {player.intelligence}")
    print(f"Luck: {player.luck}")
    print(f"Level: {player.level}")

    # Add more character details (level, experience, max hp, etc.) here
    input("Press Enter to return to the main menu...")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner_text = pyfiglet.figlet_format("Pyrim", font="epic")
    print(Fore.MAGENTA + banner_text)

    print(Fore.CYAN + format_text("~~~~~~~~~~~~~~~/Welcome To Pyrim!\~~~~~~~~~~~~~~~~"))
    print(Fore.CYAN + format_text("              The Python Skyrim RPG"))
    print(Fore.MAGENTA + format_text("        Coded by Void/GhostFace/Neo/Phantom"))
    name = input("Enter your character's Name: ")
    age = input("Enter your character's Age: ")
    eye = input("Enter your character's Eye Color: ")
    height = input("Enter your character's Height: ")
    country = input("Enter your character's country of origin: ")
    race = input("Enter your character's race: ")


    # Complete Character class selection
    character_classes = [
        "Thief", "Mage", "Warrior", "Ranger", "Paladin", "Necromancer",
        "Bard", "Druid", "Monk", "Assassin", "Cleric", "Alchemist",
        "Sorcerer", "Knight", "Warlock", "Barbarian", "Archer", "Illusionist"
    ]
    print(Fore.CYAN + format_text("~~~~~~~~~~~~~~~/Choose your class:\~~~~~~~~~~~~~~~"))
    for index, character_class in enumerate(character_classes, start=1):
        print(f" {index}. {character_class}")

    class_choice = input("Enter the number of your class: ")
    
    character_class = ""
    try:
        class_choice = int(class_choice)
        if 1 <= class_choice <= len(character_classes):
            character_class = character_classes[class_choice - 1]
        else:
            raise ValueError
    except ValueError:
        print("Invalid class choice. Defaulting to Warrior.")
        character_class = "Warrior"

     # Allocate attributes
    strength, dexterity, wisdom, intelligence, luck = allocate_attributes()
    
    player = Player(name, age, country, race, eye, height, character_class, strength, dexterity, wisdom, intelligence, luck)
    
    while True:
        print(Fore.CYAN + format_text("~~~~~~~~~~~~~~~~~~~/Main Menu:\~~~~~~~~~~~~~~~~~~~"))
        print(Fore.GREEN + "1. Explore (Mostly Funtional)")
        print(Fore.MAGENTA + "2. Shop (Under Service)")
        print(Fore.YELLOW + "3. Quests (Operational)")
        print(Fore.BLUE + "4. Character")  # Added the Character option
        print(Fore.RED + "5. Exit")

        choice = input("Choose an option (1/2/3/4/5): ")

        if choice == "1":
            explore_menu(player)
        elif choice == "2":
            shop_menu(player)
        elif choice == "3":
            quest = Quest(player)
            quest.start_quest()
        elif choice == "4":
            display_character_info(player)  # Added the function to display character info
        elif choice == "5":
            print(Fore.RED + format_text("Thank you for playing Pyrim!"))
            break
        else:
            print(Fore.RED + format_text("Invalid choice. Please try again."))



if __name__ == "__main__":
    main()
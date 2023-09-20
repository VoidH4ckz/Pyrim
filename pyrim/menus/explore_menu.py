# Pyrim/menus/explorer_menu.py
import os
import story
import random
from colorama import Fore
from utils import format_text
from characters.monster import Monster
from characters.player import display_combat_stats

def explore_menu(player):
    while True:
        print(Fore.GREEN + format_text("~~~~~~~~~~~~~~~~~/Explore Menu:\~~~~~~~~~~~~~~~~~~"))
        print(Fore.CYAN + "1. Travel (Operational)")
        print(Fore.YELLOW + "2. Fight Monsters (Under Service)")
        print(Fore.BLUE + "3. Explore (Under Service)")
        print(Fore.RED + "4. Return to Main Menu")

        choice = input("Choose an option (1 - 4): ")

        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.MAGENTA + format_text("You embark on to distant lands (Story Generating!)"))
            print(Fore.CYAN + format_text(story.generate_story()))
        elif choice == "2":
            while True:
                print(format_text("You encounter some monsters along the way!"))

                # Generate a random number of monsters (1 to 3, for example)
                num_monsters = random.randint(1, 3)

                # Create a list of random monsters with randomized classes
                possible_monsters = [
                    ("Goblin", 5, random.randint(30, 50)),
                    ("Orc", 8, random.randint(40, 60)),
                    ("Skeleton", 3, random.randint(20, 40)),
                    ("Dragon", 15, random.randint(100, 200)),
                    ("Phoenix", 12, random.randint(80, 150)),
                    ("Banshee", 7, random.randint(50, 100)),
                    ("Kitsune", 6, random.randint(40, 80)),
                    ("Cerberus", 10, random.randint(90, 160)),
                    ("Minotaur", 9, random.randint(70, 130)),
                    ("Griffin", 8, random.randint(60, 110)),
                    ("Kraken", 13, random.randint(120, 220)),
                    ("Hydra", 12, random.randint(100, 180)),
                    ("Siren", 6, random.randint(40, 80)),
                    ("Hippogriff", 7, random.randint(50, 95)),
                    ("Chimera", 11, random.randint(85, 150)),
                    ("Harpy", 5, random.randint(35, 70)),
                    ("Centaur", 6, random.randint(45, 85)),
                    ("Cyclops", 10, random.randint(80, 140)),
                    ("Gorgon", 9, random.randint(70, 130)),
                    ("Fairy", 4, random.randint(30, 60)),
                    ("Mermaid", 5, random.randint(40, 75)),
                    ("Giant", 12, random.randint(90, 170)),
                    ("Pegasus", 7, random.randint(55, 105)),
                    ("Leprechaun", 3, random.randint(25, 50)),
                    ("Unicorn", 8, random.randint(65, 120)),
                    ("Wraith", 6, random.randint(45, 85)),
                    ("Satyr", 5, random.randint(40, 75)),
                    ("Basilisk", 9, random.randint(70, 130)),
                    ("Wyvern", 10, random.randint(80, 150)),
                    ("Yeti", 7, random.randint(55, 105)),
                    ("Vampire", 11, random.randint(85, 160)),
                    ("Manticore", 8, random.randint(60, 115)),
                    ("Golem", 12, random.randint(95, 180)),
                    ("Succubus", 6, random.randint(45, 85)),
                    ("Incubus", 6, random.randint(45, 85)),
                    ("Djinn", 11, random.randint(85, 160)),
                    ("Banshee", 5, random.randint(35, 70)),
                    ("Fenrir", 13, random.randint(100, 220)),
                    ("Kappa", 4, random.randint(30, 60)),
                    ("Nymph", 5, random.randint(35, 70)),
                    ("Gryphon", 9, random.randint(70, 130)),
                    ("Roc", 14, random.randint(110, 230)),
                ]
                encounter_monsters = [Monster(name, level, health, random.choice(["Warrior", "Berserker", "Mage", "Assassin", "Rogue", "Shadow Dancer", "Thief", "Bard", "Monk", "Druid", "Sorcerer", "Knight", "Warlock"])) for name, level, health in random.sample(possible_monsters, num_monsters)]

                for monster in encounter_monsters:
                    print(format_text(f"You encounter a {monster.monster_class} {monster.name} (Level {monster.level})"))

                    while monster.health > 0 and player.health > 0:
                        display_combat_stats(player, monster)
                        print(format_text("Battle Menu:"))
                        print("1. Use Weapon")
                        print("2. Use Item")
                        print("3. Use Magic")
                        print("4. Run Away")

                        battle_choice = input("Choose an option (1/2/3/4): ")

                        if battle_choice == "1":
                            # Player attacks
                            if player.equipped_weapon:
                                player_attack = random.randint(player.equipped_weapon.damage - 5, player.equipped_weapon.damage + 5)
                                print(format_text(f"You attack the {monster.name} with your {player.equipped_weapon.name} for {player_attack} damage."))
                                monster.health -= player_attack
                            else:
                                print(format_text("You don't have a weapon equipped."))
                        elif battle_choice == "2":
                            player.use_item("Health Potion")
                        elif battle_choice == "3":
                            player.use_magic()
                        elif battle_choice == "4":
                            print(format_text("You ran away from battle."))
                            break
                        else:
                            print(format_text("Invalid choice. Please try again."))

                        # Monster attacks
                        if monster.health > 0:
                            monster_attack = random.randint(5, 15)
                            print(format_text(f"The {monster.monster_class} {monster.name} attacks you for {monster_attack} damage."))
                            player.health -= monster_attack

                        # Display updated combat stats
                        display_combat_stats(player, monster)

                    # Check the combat result
                    if player.health <= 0:
                        print(format_text("You were defeated in battle. Game Over."))
                    else:
                        print(format_text(f"You defeated the {monster.name}!"))
                        player.gain_experience(10)  # Reward the player with experience points


                        print(f"Your Health: {player.health}")
                        print(format_text(f"Your Level: {player.level}"))
                        print(f"{monster.monster_class} {monster.name}'s Health: {monster.health}")
                        print(format_text(f"{monster.monster_class} {monster.name}'s Level: {monster.level}"))

                    # Remove defeated monster from the encounter list
                    encounter_monsters.remove(monster)

                print(format_text("You have defeated all the monsters in this encounter."))
                choice = input("Do you want to continue fighting (Y/N)? ").lower()
                if choice != 'y':
                    break
        elif choice == "3":
            player.display_inventory()  # Implement a display_inventory method
        elif choice == "4":
            return
        else:
            print(format_text("Invalid choice. Please try again."))

        explore_menu(player)

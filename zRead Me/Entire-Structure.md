#Pyrim-New/pyrim.py
import os
import pyfiglet
from colorama import Fore
from menus.explore_menu import explore_menu
from menus.shop_menu import shop_menu
from menus.quest_menu import quest_menu, Quest
from characters.player import Player
from utils import format_text

# Main game loop
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Print a styled banner at the beginning
    banner_text = pyfiglet.figlet_format("Pyrim", font="epic")
    print(Fore.MAGENTA + banner_text)

    print(format_text("~~~~~~~~~~~~~~~/Welcome To Pyrim!\~~~~~~~~~~~~~~~~"))
    print(format_text("              The Python Skyrim RPG"))
    print(format_text("        Coded by Void/GhostFace/Neo/Phantom"))
    name = input("Enter your character's name: ")
    age = input("Enter your character's age: ")
    
    # Character class selection
    print(format_text("~~~~~~~~~~~~~~~/Choose your class:\~~~~~~~~~~~~~~~"))
    print("1. Thief")
    print("2. Mage")
    print("3. Warrior")
    class_choice = input("Enter the number of your class: ")
    
    character_class = ""
    if class_choice == "1":
        character_class = "Thief"
    elif class_choice == "2":
        character_class = "Mage"
    elif class_choice == "3":
        character_class = "Warrior"
    else:
        print("Invalid class choice. Defaulting to Warrior.")
        character_class = "Warrior"
    
    player = Player(name, age, character_class)
    
    while True:
    
        print(format_text("~~~~~~~~~~~~~~~~~~~/Main Menu:\~~~~~~~~~~~~~~~~~~~"))
        print("1. Explore")
        print("2. Shop")
        print("3. Quests")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == "1":
            explore_menu(player)
        elif choice == "2":
            shop_menu(player)
        elif choice == "3":
            quest = Quest(player)
            quest.start_quest()
        elif choice == "4":
            print(format_text("Thank you for playing Pyrim!"))
            break
        else:
            print(format_text("Invalid choice. Please try again."))

if __name__ == "__main__":
    main()

#Pyrim-New/utils.py
import pyfiglet
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Define a function to add spacing and separators to text
def format_text(text):
    return f"{'*' * 50}\n{text}\n{'*' * 50}\n"

#Pyrim-New/story.py

import openai

def generate_story():
    # Configure OpenAI API with your API key
    api_key = "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"
    openai.api_key = api_key

    # Define the prompt for the story
    prompt = "can you give me a 5 line story about traveling in the world of Pyrim?"

    # Generate a story using a chat model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the appropriate chat model
        messages=[
            {"role": "system", "content": "You are a brave adventurer."},
            {"role": "user", "content": prompt},
        ],
    )

    # Extract the generated story from the API response
    story = response['choices'][0]['message']['content']

    return story

#Pyrim-New/menus/explorer_menu.py
import os
import story
import random
from utils import format_text
from characters.player import Player
from characters.monster import Monster

def explore_menu(player):
    print(format_text("~~~~~~~~~~~~~~~~~/Explore Menu:\~~~~~~~~~~~~~~~~~~"))
    print("1. Travel")
    print("2. Fight Monsters")
    print("3. Explore")
    print("4. Return to Main Menu")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(format_text("You embark on to distant lands (Story Generating!)"))
        print(format_text(story.generate_story()))
    elif choice == "2":
        while True:
            print(format_text("You encounter some monsters along the way!"))

            # Generate a random number of monsters (1 to 3, for example)
            num_monsters = random.randint(1, 3)

            # Create a list of random monsters with randomized classes
            possible_monsters = [
                ("Goblin", 5, random.randint(30, 50)),
                ("Orc", 8, random.randint(40, 60)),
                ("Skeleton", 3, random.randint(20, 40))
            ]
            encounter_monsters = [Monster(name, level, health, random.choice(["Warrior", "Berserker", "Mage"])) for name, level, health in random.sample(possible_monsters, num_monsters)]

            for monster in encounter_monsters:
                print(format_text(f"You encounter a {monster.monster_class} {monster.name} (Level {monster.level})"))
                
                while monster.health > 0:
                    print(format_text("Battle Menu:"))
                    print("1. Use Weapon")
                    print("2. Use Item")
                    print("3. Use Magic")
                    print("4. Run Away")
    
                    battle_choice = input("Choose an option (1/2/3/4): ")

                    if battle_choice == "1":
                        if player.equipped_weapon:
                            player_attack = random.randint(player.equipped_weapon.damage - 5, player.equipped_weapon.damage + 5)
                            print(format_text(f"You attack the {monster.name} with your {player.equipped_weapon.name} for {player_attack} damage."))
                        else:
                            print(format_text("You don't have a weapon equipped."))
                    elif battle_choice == "2":
                        player.use_item("Health Potion")
                    elif battle_choice == "3":
                        player.use_magic()
                    elif battle_choice == "4":
                        print(format_text("You ran away from battle."))
                        break
                    elif battle_choice == "5":
                        if "Steel Sword" in player.inventory:
                            player.equip_weapon(player.inventory["Steel Sword"])
                        else:
                            print(format_text("You don't have a Steel Sword in your inventory."))
                    else:
                            print(format_text("Invalid choice. Please try again."))
                            continue

                    if monster.health <= 0:
                        print(format_text(f"You defeated the {monster.name}!"))
                        player.gain_experience(10)  # Reward the player with experience points
                        break

                    monster_attack = random.randint(5, 15)
                    print(format_text(f"The {monster.monster_class} {monster.name} attacks you for {monster_attack} damage."))
                    player.health -= monster_attack

                    if player.health <= 0:
                        print(format_text("You were defeated in battle. Game Over."))
                        exit()

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

#Pyrim-New/menus/shop_menu.py
from utils import format_text
from characters.player import Player
from items.item import Item
from items.potion import Potion
from items.weapon import Weapon
# Shop Clas
class Shop:
    def __init__(self):
        self.items = {
            Potion("Health Potion", "Restores health when consumed."): 10,
            Item("Magic Scroll", "A scroll containing magical spells."): 15,
            Weapon("Steel Sword", 25, "A sturdy steel sword."): 30,
            Weapon("Shadow Dagger", 20, "A mysterious dagger with shadowy powers."): 25,
        }

    def display_items(self):
        print(format_text("Shop Inventory:"))
        for item, price in self.items.items():
            print(format_text(f"{item}: {price} gold"))

# Shop Menu
def shop_menu(player):
    shop = Shop()
    
    while True:
        print(format_text("Shop Menu:"))
        print(format_text("1. Buy"))
        print(format_text("2. Sell"))
        print(format_text("3. Check Inventory"))
        print(format_text("4. Return to Main Menu"))
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == "1":
            shop.display_items()
            item = input("What would you like to buy? (enter item name or 'exit' to leave): ").capitalize()
            
            if item in shop.items:
                cost = shop.items[item]
                if player.gold >= cost:
                    player.add_item_to_inventory(item)
                    player.gold -= cost
                    print(format_text(f"You bought {item} for {cost} gold."))
                else:
                    print(format_text("You don't have enough gold to buy that!"))
            elif item == "exit":
                break
            else:
                print(format_text("Invalid item name."))
        elif choice == "2":
            # Implement selling logic if needed
            print(format_text("Selling feature not implemented yet."))
        elif choice == "3":
            print(format_text("\nYour Inventory:"))
            for item, quantity in player.inventory.items():
                print(format_text(f"{item}: {quantity}"))
        elif choice == "4":
            break
        else:
            print(format_text("Invalid choice. Please try again."))

#Pyrim-New/menus/quest_menu.py
import random
from utils import format_text
# Quest class
class Quest:
    def __init__(self, player):
        self.player = player
    
    def start_quest(self):
        print(format_text("Available Quests:"))
        print("1. Defeat the Goblin King")
        print("2. Retrieve the Lost Artifact")
        quest_choice = input("Choose a quest (1/2): ")
        
        if quest_choice == "1":
            self.quest_goblin_king()
        elif quest_choice == "2":
            self.quest_lost_artifact()
        else:
            print(format_text("Invalid quest choice. Please try again."))
            self.start_quest()
    
    def quest_goblin_king(self):
        print(format_text("You accept the quest to defeat the Goblin King!"))
        input("Press Enter to begin your journey...")
        
        # Simulated combat with the Goblin King
        goblin_king_health = 100
        while goblin_king_health > 0:
            player_attack = random.randint(15, 25)
            goblin_king_attack = random.randint(10, 20)
            
            print(format_text("Battle Menu:"))
            print("1. Use Weapon")
            print("2. Use Item")
            print("3. Use Magic")
            print("4. Run Away")
            
            choice = input("Choose an option (1/2/3/4): ")
            
            if choice == "1":
                print(format_text(f"You attack the Goblin King for {player_attack} damage."))
                goblin_king_health -= player_attack
            elif choice == "2":
                self.use_item()
            elif choice == "3":
                self.use_magic()
            elif choice == "4":
                print(format_text("You ran away from battle."))
                break
            else:
                print(format_text("Invalid choice. Please try again."))
                continue
            
            if goblin_king_health <= 0:
                print(format_text("You defeated the Goblin King and retrieved the treasure!"))
                self.player.add_item_to_inventory("Treasure")
                break
            
            print(format_text(f"The Goblin King attacks you for {goblin_king_attack} damage."))
            self.player.health -= goblin_king_attack
            if self.player.health <= 0:
                print(format_text("You were defeated in battle. Quest failed."))
                return
            
            print(format_text(f"Your Health: {self.player.health}"))
            print(format_text(f"Goblin King's Health: {goblin_king_health}"))
        
        input("Press Enter to continue your adventures...")
        self.start_quest()

    def quest_lost_artifact(self):
        print(format_text("You accept the quest to retrieve the Lost Artifact!"))
        input("Press Enter to start your quest...")
        
        # Simulated quest completion
        print(format_text("You search the haunted forest and find the Lost Artifact!"))
        self.player.add_item_to_inventory("Lost Artifact")
        
        input("Press Enter to continue your adventures...")
        self.start_quest()

#Pyrim-New/items/potion.py
# Potion Class

class Potion:
    def __init__(self, name, description):
        self.name = name
        self.description = description

#Pyrim-New/items/item.py
# Item Class

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

#Pyrim-New/items/weapon.py
# Weapon Class

class Weapon:
    def __init__(self, name, damage, description):
        self.name = name
        self.damage = damage
        self.description = description

#Pyrim-New/characters/player.py
import random

from utils import format_text
from characters.potion import Potion
from characters.items import Item
from characters.weapon import Weapon
# Player class
class Player:
    def __init__(self, name, age, character_class):
        self.name = name
        self.age = age
        self.character_class = character_class
        self.health = 100
        self.level = 1
        self.experience = 0
        self.inventory = {
            "Health Potion": 3,
            "Magic Scroll": 2,
        }
        self.gold = 50
        self.equipped_weapon = None  # Initially, the player has no equipped weapon
    
    #Logic to tell the game what to do when you use items
    def use_item(self, item_name):
        if item_name in self.inventory and self.inventory[item_name] > 0:
            if isinstance(self.items[item_name], Potion):
                self.consume_potion(item_name)
            elif isinstance(self.items[item_name], Item):
                self.use_magic_scroll(item_name)
            else:
                print(format_text("Item usage feature not implemented for this item."))
        else:
            print(format_text("You don't have that item in your inventory."))

    #Logic to tell the game what to do when you consume potions
    def consume_potion(self, potion_name):
        if isinstance(self.items[potion_name], Potion):
            self.health += random.randint(20, 30)
            if self.health > 100:
                self.health = 100
            self.inventory[potion_name] -= 1
            print(format_text(f"You used a {potion_name} and restored some health. Your health is now {self.health}."))
    
    #Logic to use magic scrolls
    def use_magic_scroll(self, scroll_name):
        if isinstance(self.items[scroll_name], Item):
            print(format_text(f"You used a {scroll_name} to cast a spell!"))
            # Implement spell effects here

    #Logic To equip weapons
    def equip_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.equipped_weapon = weapon
            print(format_text(f"You've equipped the {weapon.name}."))
        else:
            print(format_text("Invalid weapon selection."))
    
    #Logic to put items in your inventory
    def add_item_to_inventory(self, item, quantity=1):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
    
    #Logic to take item from your inventory
    def remove_item_from_inventory(self, item, quantity=1):
        if item in self.inventory:
            if self.inventory[item] >= quantity:
                self.inventory[item] -= quantity
            else:
                print(format_text("You don't have enough of that item."))
        else:
            print(format_text("You don't have that item in your inventory."))

    # Logic that tells the game how you gain experience.
    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= 100:  # Example threshold for leveling up
            self.level_up()
    #Level Up Logic
    def level_up(self):
        self.level += 1
        self.experience = 0
        # You can add more logic here for stat increases when leveling up    
    
    #Logic To Display Stats
    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Class: {self.character_class}")
        print(f"Health: {self.health}")
        print(f"Gold: {self.gold}")

    def use_item(self, item):
        if item in self.inventory and self.inventory[item] > 0:
            if item == "Health Potion":
                self.health += random.randint(20, 30)
                if self.health > 100:
                    self.health = 100
                self.inventory[item] -= 1
                print(format_text(f"You used a {item} and restored some health. Your health is now {self.health}."))
            elif item == "Magic Scroll":
                print(format_text(f"You used a {item} to cast a spell!"))
                # Implement spell effects here
            else:
                print(format_text("Item usage feature not implemented for this item."))
        else:
            print(format_text("You don't have that item in your inventory."))
    
    #Logic to use magic
    def use_magic(self):
        print(format_text("Magic Menu:"))
        print("1. Fireball (Cost: 10 MP)")
        print("2. Heal (Cost: 20 MP)")
        
        magic_choice = input("Choose a magic spell (1/2): ")
        
        if magic_choice == "1":
            if "Magic Scroll" in self.player.inventory and self.player.inventory["Magic Scroll"] > 0:
                if self.player.magic_points >= 10:
                    # Implement Fireball spell effect here
                    self.player.magic_points -= 10
                    print(format_text("You cast Fireball!"))
                else:
                    print(format_text("You don't have enough MP to cast Fireball."))
            else:
                print(format_text("You don't have a Magic Scroll to cast Fireball."))
        elif magic_choice == "2":
            if self.player.magic_points >= 20:
                # Implement Heal spell effect here
                self.player.magic_points -= 20
                print(format_text("You cast Heal and restored some health."))
                self.player.health += random.randint(20, 30)
                if self.player.health > 100:
                    self.player.health = 100
            else:
                print(format_text("You don't have enough MP to cast Heal."))
        else:
            print(format_text("Invalid magic choice."))
            self.use_magic()
    

#Pyrim-New/characters/monster.py
# Monster Class

class Monster:
    def __init__(self, name, level, health, monster_class):
        self.name = name
        self.level = level
        self.health = health
        self.monster_class = monster_class


This is my current code setup. can you please look it over and see if its compatable? each separation is a new file
The directory scheme looks like this

Pyrim/
│
├── main.py
├── menus/
│   ├── explore_menu.py
│   ├── shop_menu.py
│   ├── quest_menu.py
│   └── __init__.py
├── characters/
│   ├── player.py
│   ├── monster.py
│   └── __init__.py
├── items/
│   ├── potion.py
│   ├── item.py
│   ├── weapon.py
│   └── __init__.py
├── story.py
├── utils.py
└── __init__.py
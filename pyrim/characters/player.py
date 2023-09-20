import random
from utils import format_text
from items.potion import Potion
from items.item import Item
from items.weapon import Weapon
from characters.companion import companions_to_unlock

class Player:
    def __init__(self, name, age, country, race, eye, height, character_class, strength, dexterity, wisdom, intelligence, luck):
        self.level = 1
        self.experience = 0
        self.max_health = 100
        self.health = self.max_health
        self.name = name
        self.age = age
        self.country = country
        self.race = race
        self.eye = eye
        self.height = height
        self.character_class = character_class
        self.strength = strength
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.luck = luck
        self.gold = 50
        self.equipped_weapon = None  # Initially, the player has no equipped weapon
        self.inventory = {
            Potion("HealthPotion", "Restores health when consumed."): 10,
            Item("MagicScroll", "A scroll containing magical spells."): 15,
            Weapon("SteelSword", 25, "A sturdy steel sword."): 30,
        }


    # Example method to calculate damage bonus based on attributes
    def calculate_damage_bonus(self):
        return self.strength * 2  # Adjust the multiplier as needed

    # Logic to tell the game what to do when you use items
    def use_item(self, item_name):
        if item_name in self.inventory:
            item = self.inventory[item_name]
            if isinstance(item, Item):
                # Implement the logic for using the item (e.g., restoring health)
                print(format_text(f"You used {item_name}."))
                del self.inventory[item_name]
            else:
                print(format_text("You cannot use this item."))
        else:
            print(format_text("Item not found in inventory."))

    # Logic to tell the game what to do when you consume potions
    def consume_potion(self, potion_name):
        if isinstance(self.inventory[potion_name], Potion):
            self.health += random.randint(20, 30)
            if self.health > 100:
                self.health = 100
            self.inventory[potion_name] -= 1
            print(format_text(f"You used a {potion_name} and restored some health. Your health is now {self.health}."))

    # Logic to use magic scrolls
    def use_magic_scroll(self, scroll_name):
        if isinstance(self.inventory[scroll_name], Item):
            print(format_text(f"You used a {scroll_name} to cast a spell!"))
            # Implement spell effects here

    # Logic To equip weapons
    def equip_weapon(self, weapon_name):
        if weapon_name in self.inventory:
            weapon = self.inventory[weapon_name]
            if isinstance(weapon, Weapon):
                if self.equipped_weapon:
                    # Remove the currently equipped weapon and add it back to inventory
                    self.add_item_to_inventory(self.equipped_weapon)
                # Equip the new weapon
                self.equipped_weapon = weapon
                del self.inventory[weapon_name]
                print(format_text(f"You have equipped {weapon.name}."))
            else:
                print(format_text("You can only equip weapons."))
        else:
            print(format_text("Item not found in inventory."))

    # Logic to put items in your inventory
    def add_item_to_inventory(self, item, quantity=1):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    # Logic to take item from your inventory
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

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.max_health += 10  # Increase max health upon leveling up
        self.health = self.max_health  # Fully restore health upon leveling up

    # Logic to use magic
    def use_magic(self):
        print(format_text("Magic Menu:"))
        print("1. Fireball (Cost: 10 MP)")
        print("2. Heal (Cost: 20 MP)")

        magic_choice = input("Choose a magic spell (1/2): ")

        if magic_choice == "1":
            if "Magic Scroll" in self.inventory and self.inventory["Magic Scroll"] > 0:
                if self.magic_points >= 10:
                    # Implement Fireball spell effect here
                    self.magic_points -= 10
                    print(format_text("You cast Fireball!"))
                else:
                    print(format_text("You don't have enough MP to cast Fireball."))
            else:
                print(format_text("You don't have a Magic Scroll to cast Fireball."))
        elif magic_choice == "2":
            if self.magic_points >= 20:
                # Implement Heal spell effect here
                self.magic_points -= 20
                print(format_text("You cast Heal and restored some health."))
                self.health += random.randint(20, 30)
                if self.health > 100:
                    self.health = 100
            else:
                print(format_text("You don't have enough MP to cast Heal."))
        else:
            print(format_text("Invalid magic choice."))
            self.use_magic()

    # Logic to check if you are at a level to unlock a companion
    def check_companion_unlocks(self):
        # Check if any companions should be unlocked at the current level
        for companion in companions_to_unlock:
            companion.unlock(self.level)

def display_combat_stats(player, monster):
    print("\nCombat Stats:")
    print(f"Player: {player.name} (Level {player.level}) | (Class: {player.character_class})")
    print(f"Health: {player.health}/{player.max_health}")

    print("\nMonster:")
    print(f"Name: {monster.name} (Level {monster.level}) | (Class: {monster.monster_class})")
    print(f"Health: {monster.health}")
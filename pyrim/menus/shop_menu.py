#Pyrim/menus/shop_menu.py
from colorama import Fore
from utils import format_text
from characters.player import Player
from items.item import Item
from items.potion import Potion  # Import the Potion class
from items.weapon import Weapon

# Shop Class
class Shop:
    def __init__(self):
        self.items = {
            Potion("Health Potion", "Restores health when consumed."): 10,
            Potion("Mana Elixir", "Restores mana when consumed."): 8,
            Potion("Strength Tonic", "Temporarily boosts your physical strength."): 5,
            Potion("Agility Elixir", "Enhances your speed and reflexes for a short duration."): 5,
            Potion("Invisibility Potion", "Grants temporary invisibility."): 3,
            Potion("Greater Health Potion", "Restores a significant amount of health."): 6,
            Potion("Greater Mana Elixir", "Restores a significant amount of mana."): 5,
            Potion("Invincibility Elixir", "Grants temporary invincibility."): 4,
            Potion("Dragon's Blood Potion", "Boosts your strength to dragon-like levels."): 2,
            Potion("Elixir of Wisdom", "Enhances your intelligence and wisdom."): 3,
            Potion("Elixir of Invisibility", "Grants prolonged invisibility."): 2,
            Potion("Titan's Strength Tonic", "Enormously boosts your physical strength."): 3,
            Potion("Ethereal Evasion Elixir", "Allows you to phase through solid objects."): 1,
            Potion("Phoenix Rebirth Elixir", "Brings you back to life once if you die."): 2,
            Potion("Elixir of Eternal Youth", "Halts aging and grants longevity."): 2,
            Item("Magic Scroll", "A scroll containing magical spells."): 15,
            Item("Torch", "A lit torch to illuminate dark areas."): 20,
            Item("Lockpick Set", "Allows you to pick locks."): 10,
            Item("Compass", "Helps you navigate through unknown terrain."): 12,
            Item("Lucky Charm", "Brings good luck to its possessor."): 7,
            Item("Enchanted Amulet", "Provides protection against curses."): 8,
            Item("Crystal Ball", "Allows you to scry distant locations."): 6,
            Item("Satchel of Holding", "Expands your inventory capacity."): 5,
            Item("Dragon Scale Armor", "Provides excellent protection against fire."): 4,
            Item("Map of the Unknown", "Reveals uncharted territories."): 7,
            Item("Cursed Medallion", "Brings misfortune and curses to its bearer."): 1,
            Item("Whispering Gemstone", "Communicates with ancient spirits."): 4,
            Item("Enchanted Quiver", "Automatically replenishes arrows."): 6,
            Item("Mirror of Reflection", "Reflects magical attacks back at the caster."): 3,
            Item("Starlight Lantern", "Illuminates the darkest of dungeons."): 5,
            Weapon("Steel Sword", 25, "A sturdy steel sword."): 30,
            Weapon("Shadow Dagger", 20, "A mysterious dagger with shadowy powers."): 25,
            Weapon("Iron Sword", 40, "A sturdy Iron sword."): 50,
            Weapon("Shadow Dagger", 20, "A mysterious dagger with shadowy powers."): 25,
            Weapon("Mystic Staff", 35, "A staff infused with arcane energies."): 28,
            Weapon("Silver Bow", 30, "A finely crafted silver bow."): 22,
            Weapon("Flaming Axe", 40, "An axe engulfed in flames."): 18,
            Weapon("Soul Reaver Sword", 50, "A sword that consumes the souls of your foes."): 10,
            Weapon("Thunderstrike Hammer", 45, "Delivers devastating electric shocks."): 12,
            Weapon("Venomous Dagger", 35, "Poisonous blade that inflicts deadly toxins."): 14,
            Weapon("Staff of the Archmage", 60, "Harnesses the power of a master wizard."): 8,
            Weapon("Crystal Bow of Accuracy", 55, "Never misses its target."): 9,
            Weapon("Blade of Chaos", 70, "Unleashes chaotic energy with every strike."): 7,
            Weapon("Frostbite Sword", 55, "Freezes enemies with a touch."): 8,
            Weapon("Scepter of Time", 75, "Controls the flow of time itself."): 6,
            Weapon("Divine Bow of Serenity", 65, "Calms the chaos of battle."): 7,
            Weapon("DoombringerScythe", 80, "Harvests the souls of the fallen."): 100,
        }

    def display_items(self):
        print(format_text("Shop Inventory:"))
        for item, price in self.items.items():
            print(f"{item}: {price} gold")

# Shop Menu
def shop_menu(player):
    shop = Shop()
    
    while True:
        print(Fore.MAGENTA + format_text("Shop Menu:"))
        print(Fore.BLUE + "1. Buy")
        print(Fore.YELLOW + "2. Sell")
        print(Fore.GREEN + "3. Check Inventory")
        print(Fore.RED + "4. Return to Main Menu")
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == "1":
            # Display the shop inventory with formatted output
            for item, price in shop.items.items():
                item_name = item.name
                item_price = price
                print(f"{item_name}: {item_price} gold")

            item_choice = input("What would you like to buy? (Enter item name or 'exit' to leave): ").capitalize()

            if item_choice in shop.items:
                cost = shop.items[item_choice]
                if player.gold >= cost:
                    player.add_item_to_inventory(item_choice)
                    player.gold -= cost
                    print(format_text(f"You bought {item_choice} for {cost} gold."))
                else:
                    print(format_text("You don't have enough gold to buy that!"))
            elif item_choice == "Exit":
                break
            else:
                print(format_text("Invalid item name."))
        elif choice == "2":
            # Implement selling logic if needed
            print(format_text("Selling feature not implemented yet."))
        elif choice == "3":
            while True:
                print(Fore.GREEN + format_text("Inventory Menu:"))
                print(Fore.BLUE + "1. Equip Weapon")
                print(Fore.YELLOW + "2. Use Item")
                print(Fore.RED + "3. Return to Shop Menu")
                
                inventory_choice = input("Choose an option (1/2/3): ")
                
                if inventory_choice == "1":
                    # Display the player's inventory and allow them to equip a weapon
                    print(Fore.CYAN + format_text("\nYour Inventory:"))
                    for item, quantity in player.inventory.items():
                        print(f"{item.name}: {quantity}")
                    
                    weapon_choice = input("Enter the name of the weapon to equip or 'exit': ").capitalize()
                    if weapon_choice == "Exit":
                        break
                    else:
                        player.equip_weapon(weapon_choice)
                elif inventory_choice == "2":
                    # Display the player's inventory and allow them to use an item/potion
                    print(Fore.CYAN + format_text("\nYour Inventory:"))
                    for item, quantity in player.inventory.items():
                        print(f"{item}: {quantity}")
                    
                    item_choice = input("Enter the name of the item/potion to use or 'exit': ").capitalize()
                    if item_choice == "Exit":
                        break
                    else:
                        player.use_item(item_choice)
                elif inventory_choice == "3":
                    break
                else:
                    print(format_text("Invalid choice. Please try again."))
        elif choice == "4":
            break
        else:
            print(format_text("Invalid choice. Please try again."))

    shop_menu(player)
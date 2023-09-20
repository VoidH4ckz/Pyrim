#Pyrim-New/menus/quest_menu.py
import random
from utils import format_text

# Quest class
class Quest:
    def __init__(self, player):
        self.player = player
    
    def start_quest(self):
        print(format_text("Available Quests:"))
        print(" 1. Defeat the Goblin King")
        print(" 2. Retrieve the Lost Artifact")
        print(" 3. The Enchanted Sword")
        print(" 4. The Cursed Amulet")
        print(" 5. Cursed Mansion Investigation")
        print(" 6. Hunt For The Elemental Crystal")
        print(" 7. Pirate's Treasure Hunt")
        print(" 8. Lost Relic Expedition")
        print(" 9. Haunted Castle Quest")
        print("10. Enchanted Forest Quest")
        print("11. Bandit King's Heist")
        print("12. Dragon's Lair")
        print("13. The Lost Relic Quest")
        print("14. The Dragon's Hoard")
        print("15. Back To Main Menu")

        quest_choice = input("Choose a quest (1 - 15): ")
        
        if quest_choice == "1":
            self.quest_goblin_king()
        elif quest_choice == "2":
            self.quest_lost_artifact()
        elif quest_choice == "3":
            self.quest_enchanted_sword()
        elif quest_choice == "4":
            self.quest_cursed_amulet()
        elif quest_choice == "5":
            self.quest_cursed_mansion_investigation()
        elif quest_choice == "6":
            self.quest_elemental_crystal()
        elif quest_choice == "7":
            self.quest_pirates_treasure_hunt()
        elif quest_choice == "8":
            self.quest_lost_relic_expedition()
        elif quest_choice == "9":
            self.quest_haunted_castle()
        elif quest_choice == "10":
            self.quest_enchanted_forest()
        elif quest_choice == "11":
            self.quest_bandit_kings_heist()
        elif quest_choice == "12":
            self.quest_dragons_lair()
        elif quest_choice == "13":
            self.quest_lost_relic()
        elif quest_choice == "14":
            self.quest_dragons_hoard()
        elif quest_choice == "15":
            return
        else:
            print(format_text("Invalid quest choice. Please try again."))
            self.start_quest()

   ### Combat Quests. Keep Scrolling For Text Based Quests ###         
# Goblin King Quest   
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
            print("5. Check Inventory and Equip Items")  # Added option to check inventory and equip items
        
            choice = input("Choose an option (1/2/3/4/5): ")
        
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
            elif choice == "5":
                self.check_inventory_and_equip_items()  # Call the method to check and equip items
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

# Dragons Lair Quest
    def quest_dragons_lair(self):
        print(format_text("You accept the quest to slay the fearsome Dragon in its lair!"))
        input("Press Enter to begin your journey...")
    
        # Simulated combat with the Dragon
        dragon_health = 150
        while dragon_health > 0:
            player_attack = random.randint(20, 30)
            dragon_attack = random.randint(15, 25)
        
            print(format_text("Battle Menu:"))
            print("1. Use Weapon")
            print("2. Use Item")
            print("3. Use Magic")
            print("4. Run Away")
            print("5. Check Inventory and Equip Items")
        
            choice = input("Choose an option (1/2/3/4/5): ")
        
            if choice == "1":
                print(format_text(f"You strike the Dragon for {player_attack} damage."))
                dragon_health -= player_attack
            elif choice == "2":
                self.use_item()
            elif choice == "3":
                self.use_magic()
            elif choice == "4":
                print(format_text("You bravely flee from the Dragon's lair."))
                break
            elif choice == "5":
                self.check_inventory_and_equip_items()
            else:
                print(format_text("Invalid choice. Please try again."))
                continue
        
            if dragon_health <= 0:
                print(format_text("You triumph over the Dragon and claim its hoard!"))
                self.player.add_item_to_inventory("Dragon's Hoard")
                break
        
            print(format_text(f"The Dragon breathes fire at you, dealing {dragon_attack} damage."))
            self.player.health -= dragon_attack
            if self.player.health <= 0:
                print(format_text("You were incinerated by the Dragon's flames. Quest failed."))
                return
        
            print(format_text(f"Your Health: {self.player.health}"))
            print(format_text(f"Dragon's Health: {dragon_health}"))
    
        input("Press Enter to continue your adventures...")
        self.start_quest()

# Bandit King's Heist Quest

    def quest_bandit_kings_heist(self):
        print(format_text("You accept the quest to recover the stolen treasure from the Bandit King!"))
        input("Press Enter to begin your journey...")
    
        # Infiltration and combat with bandits
        bandit_king_health = 120
        while bandit_king_health > 0:
            player_attack = random.randint(10, 20)
            bandit_king_attack = random.randint(15, 25)
        
            print(format_text("Infiltration Menu:"))
            print("1. Sneak past guards")
            print("2. Fight bandits")
            print("3. Use Item")
            print("4. Use Stealth Skills")
        
            choice = input("Choose an option (1/2/3/4): ")
        
            if choice == "1":
                print(format_text("You successfully sneak past the guards and move closer to the treasure."))
            elif choice == "2":
                print(format_text(f"You engage the Bandit King's henchmen, dealing {player_attack} damage."))
                bandit_king_health -= player_attack
            elif choice == "3":
                self.use_item()
            elif choice == "4":
                print(format_text("Your stealth skills help you avoid detection for now."))
            else:
                print(format_text("Invalid choice. Please try again."))
                continue
        
            if bandit_king_health <= 0:
                print(format_text("You confront the Bandit King and retrieve the stolen treasure!"))
                self.player.add_item_to_inventory("Recovered Treasure")
                break
        
            print(format_text(f"The Bandit King's henchmen attack you for {bandit_king_attack} damage."))
            self.player.health -= bandit_king_attack
            if self.player.health <= 0:
                print(format_text("You succumb to the bandits' onslaught. Quest failed."))
                return
        
            print(format_text(f"Your Health: {self.player.health}"))
            print(format_text(f"Bandit King's Health: {bandit_king_health}"))
    
        input("Press Enter to continue your adventures...")
        self.start_quest()

# Enchanted Forest Quest

    def quest_enchanted_forest(self):
        print(format_text("You embark on the quest to explore the mystical Enchanted Forest!"))
        input("Press Enter to begin your journey...")
    
        # Encounters and puzzles in the Enchanted Forest
        forest_challenges = 3
        while forest_challenges > 0:
            print(format_text("Enchanted Forest Challenges:"))
            print("1. Solve a riddle from a talking tree")
            print("2. Navigate a maze of thorns")
            print("3. Defend against enchanted creatures")
        
            choice = input("Choose a challenge to face (1/2/3): ")
        
            if choice == "1":
                print(format_text("The talking tree presents you with a riddle. You solve it and gain wisdom."))
            elif choice == "2":
                print(format_text("You successfully navigate the thorny maze and advance deeper into the forest."))
            elif choice == "3":
                print(format_text("Enchanted creatures attack! You fend them off with your skills."))
            else:
                print(format_text("Invalid choice. Please try again."))
                continue
        
            forest_challenges -= 1
    
        print(format_text("You have conquered the challenges of the Enchanted Forest!"))
        self.player.add_item_to_inventory("Forest's Blessing")
    
        input("Press Enter to continue your adventures...")
        self.start_quest()

# Haunted Castle Quest
    def quest_haunted_castle(self):
        print(format_text("You accept the quest to investigate the Haunted Castle and banish its evil spirits!"))
        input("Press Enter to begin your journey...")
    
        # Exploration and encounters in the Haunted Castle
        ghosts_remaining = 5
        while ghosts_remaining > 0:
            print(format_text("Haunted Castle Exploration:"))
            print("1. Search for clues in the dark halls")
            print("2. Confront a ghostly apparition")
            print("3. Use holy water to cleanse")
        
            choice = input("Choose an action (1/2/3): ")
        
            if choice == "1":
                print(format_text("You uncover a cryptic message that hints at the castle's history."))
            elif choice == "2":
                print(format_text("You engage in a spectral battle with a ghost, weakening its presence."))
                ghosts_remaining -= 1
            elif choice == "3":
                print(format_text("You use holy water to cleanse a haunted room, banishing the spirits within."))
                ghosts_remaining -= 1
            else:
                print(format_text("Invalid choice. Please try again."))
                continue
    
        print(format_text("You have cleansed the Haunted Castle of its malevolent spirits!"))
        self.player.add_item_to_inventory("Castle's Redemption")
    
        input("Press Enter to continue your adventures...")
        self.start_quest()


# Lost Relic Expidition Quest
    def quest_lost_relic_expedition(self):
        print(format_text("You embark on an expedition to find a lost relic of great power!"))
        input("Press Enter to begin your journey...")
    
        # Journey through treacherous terrain and puzzles
        relic_found = False
        while not relic_found:
            print(format_text("Expedition Challenges:"))
            print("1. Cross a perilous chasm")
            print("2. Decipher ancient inscriptions")
            print("3. Face guardian creatures")
        
            choice = input("Choose a challenge to overcome (1/2/3): ")
        
            if choice == "1":
                print(format_text("You successfully navigate the treacherous chasm and continue your quest."))
            elif choice == "2":
                print(format_text("You decipher the ancient inscriptions, revealing clues to the relic's location."))
            elif choice == "3":
                print(format_text("Guardian creatures block your path! You defeat them to advance further."))
            else:
                print(format_text("Invalid choice. Please try again."))
                continue
        
            # Check if the relic is found
            relic_found = random.choice([True, False])
    
        print(format_text("You've discovered the lost relic of power!"))
        self.player.add_item_to_inventory("Ancient Relic")
    
        input("Press Enter to continue your adventures...")
        self.start_quest()
# Pirates Treasure Hunt Quest
    def quest_pirates_treasure_hunt(self):
        print(format_text("You accept the quest to search for the legendary pirate's hidden treasure!"))
        input("Press Enter to begin your journey...")
    
        # Treasure hunt challenges and pirate encounters
        treasure_found = False
        while not treasure_found:
            print(format_text("Treasure Hunt Challenges:"))
            print("1. Follow an old map")
            print("2. Solve riddles left by the pirate")
            print("3. Engage in ship-to-ship combat with pirates")
        
            choice = input("Choose a challenge to face (1/2/3): ")
        
            if choice == "1":
                print(format_text("You follow the old map's directions and get closer to the treasure's location."))
            elif choice == "2":
                print(format_text("You solve the pirate's riddles, revealing the treasure's whereabouts."))
            elif choice == "3":
                print(format_text("Pirate ships approach! You engage in a fierce naval battle to protect the treasure."))
            else:
                print(format_text("Invalid choice. Please try again."))
                continue
        
            # Check if the treasure is found
            treasure_found = random.choice([True, False])
    
        print(format_text("You've discovered the legendary pirate's treasure hoard!"))
        self.player.add_item_to_inventory("Pirate's Treasure")
    
        input("Press Enter to continue your adventures...")
        self.start_quest()

# Elemental Crystal Quest
    def quest_elemental_crystal(self):
        print(format_text("You undertake the quest to retrieve the lost Elemental Crystals and restore balance!"))
        input("Press Enter to begin your journey...")
    
        # Elemental challenges and guardians
        crystals_collected = 0
        while crystals_collected < 4:  # Collect four elemental crystals
            print(format_text("Elemental Challenges:"))
            print("1. Harness the power of fire")
            print("2. Navigate a frozen labyrinth")
            print("3. Overcome a fierce windstorm")
            print("4. Dive into the depths of an underwater cave")
        
            choice = input("Choose an elemental challenge (1/2/3/4): ")
        
            if choice == "1":
                print(format_text("You harness the power of fire, obtaining the Fire Crystal."))
                crystals_collected += 1
            elif choice == "2":
                print(format_text("You navigate the frozen labyrinth and secure the Ice Crystal."))
                crystals_collected += 1
            elif choice == "3":
                print(format_text("You brave the fierce windstorm and claim the Wind Crystal."))
                crystals_collected += 1
            elif choice == "4":
                print(format_text("You dive into the underwater cave and retrieve the Water Crystal."))
                crystals_collected += 1
            else:
                print(format_text("Invalid choice. Please try again."))
                continue
    
        print(format_text("You've collected all four Elemental Crystals, restoring balance to the world!"))
        self.player.add_item_to_inventory("Elemental Crystals")
    
        input("Press Enter to continue your adventures...")
        self.start_quest()

# Cursed Mansion Investigation Quest
    def quest_cursed_mansion_investigation(self):
        print(format_text("You accept the quest to investigate a haunted and cursed mansion!"))
        input("Press Enter to begin your journey...")
    
        # Exploration and encounters within the cursed mansion
        ghosts_defeated = 0
        while ghosts_defeated < 5:  # Defeat five ghosts to cleanse the mansion
            print(format_text("Mansion Exploration:"))
            print("1. Search for clues in the eerie library")
            print("2. Confront a malevolent ghost")
            print("3. Perform a ritual to dispel the curse")
        
            choice = input("Choose an action (1/2/3): ")
        
            if choice == "1":
                print(format_text("You find crucial clues in the haunted library, unraveling the mansion's dark history."))
            elif choice == "2":
                print(format_text("You confront a malevolent ghost and weaken its influence on the mansion."))
                ghosts_defeated += 1
            elif choice == "3":
                print(format_text("You perform a cleansing ritual, dispelling the curse from a haunted room."))
                ghosts_defeated += 1
            else:
                print(format_text("Invalid choice. Please try again."))
                continue
    
        print(format_text("You've successfully investigated and cleansed the cursed mansion!"))
        self.player.add_item_to_inventory("Cursed Mansion Cleansed")
    
        input("Press Enter to continue your adventures...")
        self.start_quest()


### Text Based Quests ###

# Lost Artifacts Quest
    def quest_lost_artifact(self):
        print(format_text("You accept the quest to retrieve the Lost Artifact!"))
        input("Press Enter to start your quest...")

        print(format_text("You embark on a perilous journey into the heart of the haunted forest, its ancient trees looming like silent guardians. Moonlight filters through the dense canopy, casting eerie shadows on your path. The air is thick with the whispers of restless spirits."))
        input("Press Enter to continue your adventure...")

        print(format_text("As you venture deeper, you notice strange symbols etched into the trees, glowing faintly with an ethereal light. They seem to guide your way, offering protection against the forest's malevolent forces."))
        input("Press Enter to follow the mystical markings...")

        # Simulated quest challenges
        print(format_text("Your quest is fraught with challenges. You must cross a rickety bridge over a chasm, facing the fear of falling into the abyss. You encounter spectral apparitions, testing your resolve. The forest itself seems to come alive, attempting to deter your progress."))
        input("Press Enter to overcome these obstacles...")

        print(format_text("Finally, you reach a hidden clearing bathed in moonlight. In its center, the Lost Artifact awaits, nestled within an ancient stone pedestal. Its radiance is enchanting, yet ominous. You approach cautiously, feeling the artifact's pulse resonate with your very soul."))
        input("Press Enter to collect the artifact...")

        print(format_text("As you grasp the Lost Artifact, a surge of energy courses through you, connecting you to the forest's spirits. They acknowledge your bravery and grant you their blessing."))
        input("Press Enter to absorb the forest's magic...")

        self.player.add_item_to_inventory("Lost Artifact")

        print(format_text("With the artifact in your possession, you begin your journey back through the haunted forest. To your astonishment, the once-hostile spirits now watch over you, guiding your way and offering a sense of protection. Your quest has brought harmony to this once-cursed place."))
        input("Press Enter to continue your adventures...")

        self.start_quest()
# Enchanted Sword Quest
    def quest_enchanted_sword(self):
        print(format_text("You accept the quest to retrieve the Enchanted Sword!"))
        input("Press Enter to embark on your quest...")

        print(format_text("Your journey takes you to the legendary Enchanted Forest, a place shrouded in mystery and magic. The ancient trees seem to whisper secrets as you tread softly beneath their towering canopies."))
        input("Press Enter to continue your adventure...")

        print(format_text("You follow the guidance of mystical fireflies that lead the way through the forest's winding paths. Their soft, glowing light illuminates your path, protecting you from lurking dangers."))
        input("Press Enter to follow the fireflies...")

        # Simulated quest challenges
        print(format_text("The forest presents you with trials, including solving riddles posed by ancient spirits and braving treacherous terrain. You encounter guardians of the Enchanted Sword who challenge your worthiness to wield it."))
        input("Press Enter to prove your mettle...")

        print(format_text("At the heart of the Enchanted Forest, you find the sacred grove where the Enchanted Sword rests, embedded in a stone plinth. It radiates a mesmerizing aura, and the forest itself seems to acknowledge your presence."))
        input("Press Enter to claim the Enchanted Sword...")

        print(format_text("As you grasp the hilt, a surge of magic courses through you, and you become one with the forest. You are now its protector and guardian, entrusted with the Enchanted Sword's immense power."))
        input("Press Enter to embrace your new role...")

        self.player.add_item_to_inventory("Enchanted Sword")

        print(format_text("With the Enchanted Sword in your possession, you feel a deep connection to the Enchanted Forest. Its creatures become your allies, and you leave the forest knowing that you are its champion."))
        input("Press Enter to continue your adventures...")

        self.start_quest()

# Cursed Amulets Quest
    def quest_cursed_amulet(self):
        print(format_text("You accept the quest to retrieve the Cursed Amulet!"))
        input("Press Enter to begin your quest...")

        print(format_text("Your quest leads you to the forbidding Shadow Swamp, a desolate place where the air is heavy with darkness. The putrid water glows with an eerie, sickly green light, revealing twisted trees and eerie creatures lurking below the surface."))
        input("Press Enter to continue your adventure...")

        print(format_text("Navigating the treacherous swamp, you encounter cryptic signs and symbols, hinting at the location of the Cursed Amulet. The swamp's ominous whispers guide your way, but you must tread carefully to avoid its deadly traps."))
        input("Press Enter to follow the ominous guidance...")

        # Simulated quest challenges
        print(format_text("Your quest is filled with peril. You must outwit the swamp's illusions, confront its guardians, and decipher ancient incantations to reach the heart of the darkness. The amulet's curse tests your resolve at every step."))
        input("Press Enter to overcome the curse...")

        print(format_text("In a hidden chamber deep within the swamp, you discover the Cursed Amulet, its malevolent aura palpable. You carefully pick it up, feeling its dark power coursing through you."))
        input("Press Enter to collect the amulet...")

        print(format_text("The amulet's curse threatens to consume you, but your determination prevails. You gain control over its dark magic, mastering it as a weapon against the shadows."))
        input("Press Enter to embrace the amulet's power...")

        self.player.add_item_to_inventory("Cursed Amulet")

        print(format_text("With the Cursed Amulet in your possession, you emerge from the Shadow Swamp, the once-frightening place now under your command. The amulet's dark magic is yours to wield, a testament to your strength and willpower."))
        input("Press Enter to continue your adventures...")

        self.start_quest()

# Dragons Hoard Quest
    def quest_dragons_hoard(self):
        print(format_text("You accept the quest to claim the Dragon's Hoard!"))
        input("Press Enter to embark on your quest...")

        print(format_text("Your journey takes you to the treacherous Dragon's Peak, a towering mountain said to be the home of a fearsome dragon. The winds howl, and the air is thin as you ascend the steep slopes, filled with dread and anticipation."))
        input("Press Enter to continue your adventure...")

        print(format_text("Guided by ancient legends and the glimmer of dragon scales, you navigate treacherous cliffs and caves. The mountain itself seems to test your determination, with avalanches and freezing storms threatening to halt your progress."))
        input("Press Enter to endure the mountain's challenges...")

        # Simulated quest challenges
        print(format_text("Your quest is a test of courage. You face fiery trials, decipher riddles set by the dragon, and navigate a labyrinth of tunnels. The dragon's hoard is heavily guarded by its fearsome minions, ready to protect their master's treasure."))
        input("Press Enter to confront the dragon's guardians...")

        print(format_text("Finally, you reach the heart of Dragon's Peak, where the dragon's hoard gleams with unimaginable wealth. The dragon itself awaits, its eyes fixed upon you, testing your worthiness to claim its treasure."))
        input("Press Enter to face the dragon...")

        print(format_text("In a battle of wits and strength, you prove yourself to the dragon and earn its respect. It allows you to take a portion of its hoard, knowing that you are a worthy challenger."))
        input("Press Enter to claim the Dragon's Hoard...")

        self.player.add_item_to_inventory("Dragon's Hoard")

        print(format_text("With a portion of the Dragon's Hoard in your possession, you descend from Dragon's Peak as a triumphant hero. The mountain and its guardian now recognize you as a formidable ally, and the dragon's treasure will aid you in your future adventures."))
        input("Press Enter to continue your adventures...")

        self.start_quest()
# The Lost Relic Quest
    def quest_lost_relic(self):
        print(format_text("You accept the quest to recover the Lost Relic!"))
        input("Press Enter to embark on your journey...")
    
        print(format_text("Your quest leads you to the enigmatic Desert of Echoes, where shifting sands conceal ancient secrets. The relentless sun beats down as you navigate the dunes, and whispers of long-forgotten tales fill the air."))
        input("Press Enter to continue your adventure...")

        print(format_text("You follow a trail of forgotten hieroglyphics etched in stone, guided by the spirits of the desert. They reveal hidden oases, mirages, and traps, testing your wit and endurance."))
        input("Press Enter to follow the desert's guidance...")

        # Simulated quest challenges
        print(format_text("The desert challenges you with mirages that deceive your senses, riddles that demand your wisdom, and sandstorms that test your resilience. Guardians of the Lost Relic guard its sanctuary, each challenging your worthiness."))
        input("Press Enter to prove your determination...")

        print(format_text("At the heart of the desert, you uncover the Lost Relic, shimmering with ancient power. It calls to you, recognizing your spirit's strength. You reach out and grasp it, feeling the desert's magic course through you."))
        input("Press Enter to claim the Lost Relic...")

        print(format_text("As you hold the Lost Relic, the desert's spirits embrace you, granting their blessings. The once-arid sands bloom with life, and you leave the desert knowing that you've brought vitality to a parched land."))
        input("Press Enter to continue your adventures...")

        self.player.add_item_to_inventory("Lost Relic")

        self.start_quest()


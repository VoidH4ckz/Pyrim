def inn(self, player):
        print("____________________________________________________________")
        print("Stepping inside the cozy inn, the gentle hum of conversation")
        print("Then the aroma of hearty meals instantly embraces you,")
        print("offering solace in the midst of your journey.")
        print("____________________________________________________________")
    
        while True:
            print("\nOptions:")
            print("1. Sleep The Night")
            print("2. Save Your Game")
            print("3. Load Your Game")
            print("4. Leave Inn")
        
            choice = input("Enter your choice: ")
        
            if choice == "1":
                print("You sleep for the night and feel refreshed and ready to go.")
                player.heal(player.max_hp - player.hp)  # Fully heal the character
            elif choice == "2":
                save_game(player)  # Call the save_game function
            elif choice == "3":
                load_game(player)  # Call the load_game function
            elif choice == "4":
                print("You leave the inn.")
                break
            else:
                print("Invalid choice. Please try again.")
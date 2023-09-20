def bank(self, player):
        print(f"_______________________________")
        print(f"Bank gold: {Fore.YELLOW}{self.bank_gold}{Fore.RESET}")
        print(f"Your gold: {Fore.YELLOW}{player.gold}{Fore.RESET}")
        print(f"_______________________________")
        while True:
            print("\nOptions:")
            print("1. Deposit gold")
            print("2. Withdraw gold")
            print("3. Leave Bank")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                amount = int(input("Enter the amount to deposit: "))
                if player.gold >= amount:
                    player.gold -= amount
                    self.bank_gold += amount
                else:
                    print("You don't have enough gold.")
            elif choice == "2":
                amount = int(input("Enter the amount to withdraw: "))
                if self.bank_gold >= amount:
                    player.gold += amount
                    self.bank_gold -= amount
                else:
                    print("The bank doesn't have enough gold.")
            elif choice == "3":
                print("You leave the bank.")
                break
            else:
                print("Invalid choice. Please try again.")
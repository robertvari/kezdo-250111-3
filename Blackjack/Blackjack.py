import os, time

class Blackjack:
    def __init__(self):
        self.clear_screen()
        self.intro()

        self.player = None
        self.computer1 = None
        self.computer2 = None
        self.computer3 = None


    def clear_screen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    
    def intro(self):
        print("-"*50, "BLACKJACK", "-"*50)
        time.sleep(1)
        print("Blackjack is a simple card game. Your only goal is to collect cards to have 21 in your hand.")
        time.sleep(1)
        input("Press Enter to continue...")


# Run game
Blackjack()
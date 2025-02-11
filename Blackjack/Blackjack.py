import os, time
from game_assets.cards import Deck
from game_assets.players import Player, Computer

class Blackjack:
    def __init__(self):
        self.clear_screen()
        self.intro()

        self.deck = Deck()

        self.players = [
            Player(),
            Computer(),
            Computer(),
            Computer()
        ]

        # create player names and credits
        for p in self.players:
            p.create()

        self.game_loop()

    def game_loop(self):
        self.clear_screen()
        self.deck.create()

        for p in self.players:
            p.init_hand(self.deck)
        
        for p in self.players:
            p.draw(self.deck)
        
        self.get_winner()
    
    def get_winner(self):
        self.clear_screen()
        winner_list = [p for p in self.players if p.hand_value <= 21]

        if not winner_list:
            print("House wins")
        else:
            sorted_winners = sorted(winner_list, key=lambda p: p.hand_value)
            winner = sorted_winners[-1]
            print(f"The winner: {winner.name}")

        response = input("Do you want to play again? (y/n)")
        if response == "y":
            self.game_loop()
        else:
            print("See you next time.")
            exit()

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
import os, random

# when a class instantiate an other class we call it compound class
class MagicNumber:
    def __init__(self):
        self.player = Player()
        self.computer = Computer()

        self.clear_screen()
        self.intro()
        self.game_loop()

    def clear_screen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    
    def intro(self):
        print("-"*50, "MAGIC NUMBERS", "-"*50)
        self.player.get_name()
        print(f"Well... hello {self.player}")
        print(f"I have a number between {self.computer.min_number} and {self.computer.max_number}. Can you guess it?")

    def game_loop(self):
        max_tries = 3

        print(f"You have {max_tries} tries.")

        self.computer.get_number()
        self.player.get_number()

        print(f"Computer number: {self.computer.magic_number}")

        while self.player.magic_number != self.computer.magic_number:
            self.clear_screen()
            max_tries -=1
            if max_tries == 0:
                self.round_end_conditions()
            
            print(f"Wrong guess. You have {max_tries} tries left.")
            self.player.get_number()
    
    def round_end_conditions(self):
        self.clear_screen()

        if self.computer.magic_number == self.player.magic_number:
            print(f"You win {self.player}! {self.computer.magic_number} was my number")
            self.player.add_coins(10)
        else:
            self.player.remove_coins(10)
            print("You lost this round :(")
        
        response = self.player.ask_next_round()
        if response == "y":
            self.clear_screen()
            self.game_loop()
        else:
            self.exit_game()

    def exit_game(self):
        self.clear_screen()
        print("See you next time!")
        exit()

class Player:
    def __init__(self):
        self.name = None
        self.coins = 100
        self.magic_number = 0
    
    def ask_next_round(self):
        return input("Do you want to play again? (y/n)")

    def add_coins(self, coins):
        self.coins += coins
        print(f"{self.name} winds {coins} coins.")
        print(f"Now you have {self.coins}")

    def remove_coins(self, coins):
        self.coins -= coins
        print(f"{self.name} loses {coins} coins.")
        print(f"Now you have {self.coins}")

    def get_name(self):
        self.name = input("What is your name? ")

    def get_number(self):
        self.magic_number = int(input("What is your number? "))

    def __str__(self):
        return self.name

class Computer:
    def __init__(self):
        self.min_number = 1
        self.max_number = 10
        self.magic_number = 0

    def get_number(self):
        self.magic_number = random.randint(self.min_number, self.max_number)

MagicNumber()
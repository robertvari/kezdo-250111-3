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
        print(f"MAGIC NUMBER: {self.computer.magic_number}")

class Player:
    def __init__(self):
        self.name = None
        self.coins = 100
    
    def get_name(self):
        self.name = input("What is your name? ")

    def __str__(self):
        return self.name

class Computer:
    def __init__(self):
        self.min_number = 1
        self.max_number = 10
        self.magic_number = random.randint(self.min_number, self.max_number)


MagicNumber()
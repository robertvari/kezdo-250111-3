import os, random

# when a class instantiate an other class we call it compound class
class MagicNumber:
    def __init__(self):
        self.player = Player()
        self.computer = Computer()
        self.min_number = 1
        self.max_number = 10

        self.clear_screen()
        self.intro()

    def clear_screen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    
    def intro(self):
        print("-"*50, "MAGIC NUMBERS", "-"*50)
        self.player.get_name()
        print(f"Well... hello {self.player}")
        print(f"I have a number between {self.min_number} and {self.max_number}. Can you guess it?")

class Player:
    def __init__(self):
        self.name = None
        self.coins = 100
    
    def get_name(self):
        self.name = input("What is your name? ")

    def __str__(self):
        return self.name

class Computer:
    pass


MagicNumber()
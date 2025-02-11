import os, random, time

# when a class instantiate an other class we call it compound class
class MagicNumber:
    def __init__(self):
        self.player = Player()
        self.computer = Computer()
        self.computer.get_name()

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
        self.clear_screen()
        print(f"Well... hello {self.player}")
        print(f"I have a number between {self.computer.min_number} and {self.computer.max_number}. Can you guess it?")

    def game_loop(self):
        max_tries = 3

        print(f"You have {max_tries} tries.")

        self.computer.get_number()
        self.player.get_number()

        while self.player.magic_number != self.computer.magic_number:
            self.clear_screen()
            max_tries -=1
            if max_tries == 0:
                self.round_end_conditions()
            
            print(f"Wrong guess. You have {max_tries} tries left.")
            self.player.get_number()
        
        self.round_end_conditions()
    
    def round_end_conditions(self):
        self.clear_screen()

        if self.computer.magic_number == self.player.magic_number:
            print(f"You win {self.player}! {self.computer.magic_number} was my number")
            self.player.add_coins(10)
            self.computer.remove_coins(10)
        else:
            self.computer.add_coins(10)
            self.player.remove_coins(10)
            print("You lost this round :(")

        if self.player.coins <= 0:
            self.clear_screen()
            print("You don't have money for the next round.")
            time.sleep(3)
            self.exit_game()
        
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



class Player_BASE:
    def __init__(self):
        self.name = None
        self.coins = 100
        self.magic_number = 0
        self.min_number = 1
        self.max_number = 10
    
    def get_number(self):
        self.magic_number = random.randint(self.min_number, self.max_number)
    
    def get_name(self):
        first_names = ["Liam", "Emma", "Noah", "Olivia", "Ethan", "Ava", "James", "Sophia", "Benjamin", "Mia"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
        self.name = f"{random.choice(first_names)} {random.choice(last_names)}"

    def add_coins(self, coins):
        self.coins += coins
        print(f"{self.name} winds {coins} coins.")
        print(f"Now you have {self.coins} coins")

    def remove_coins(self, coins):
        self.coins -= coins
        print(f"{self.name} loses {coins} coins.")
        print(f"Now you have {self.coins} coins")
    
    def __str__(self):
        return self.name

class Player(Player_BASE):
    def ask_next_round(self):
        return input("Do you want to play again? (y/n)")

    # full ovveride on get_name()
    def get_name(self):
        self.name = input("What is your name? ")

    # full override on get_number()
    def get_number(self):
        self.magic_number = int(input(f"What is your number between {self.min_number}-{self.max_number}? "))

class Computer(Player_BASE):
    pass

MagicNumber()
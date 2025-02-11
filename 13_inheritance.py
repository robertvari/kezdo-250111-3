import random

class Player_BASE:
    def __init__(self):
        self.name = None
        self.coins = 100
        self.magic_number = 0
    
    def get_number(self):
        self.magic_number = random.randint(1, 10)
    
    def get_name(self):
        first_names = ["Liam", "Emma", "Noah", "Olivia", "Ethan", "Ava", "James", "Sophia", "Benjamin", "Mia"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

        self.name = f"{random.choice(first_names)} {random.choice(last_names)}"


class Player(Player_BASE):
    # partial method override
    def __init__(self):
        # runst BASE.__init__()
        super().__init__()
        self.coins = 200000000
    
    # full override
    def get_name(self):
        self.name = input("What is your name? ")

class Computer(Player_BASE):
    pass



player = Player()
computer = Computer()

print(player.coins)
print(computer.coins)
import random

class Player_BASE:
    def __init__(self):
        self.name = None
        self.coins = 100
        self.magic_number = 0
        self.inventory = []
    
    def get_number(self):
        self.magic_number = random.randint(1, 10)
    
    def get_name(self):
        first_names = ["Liam", "Emma", "Noah", "Olivia", "Ethan", "Ava", "James", "Sophia", "Benjamin", "Mia"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]


class Player(Player_BASE):
    pass

class Computer(Player_BASE):
    pass



player = Player()
computer = Computer()
player.get_number()
computer.get_number()

print(player.name)
print(computer.name)
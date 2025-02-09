import random

class Player_BASE:
    def __init__(self):
        self.__name = None
        self.__credits = 0
        self.__hand = []
        self.__playing = True

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def create(self):
        self.__credits = random.randint(10, 100)
        self.__name = self.__get_random_name()

    def __get_random_name(self):
        first_names = ["Liam", "Emma", "Noah", "Olivia", "Ethan", "Ava", "James", "Sophia", "Benjamin", "Mia"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def __str__(self):
        return f"Name: {self.__name} Credits: {self.__credits}"

class Player(Player_BASE):
    def create(self):
        super().create()
        self.name = input("What is your name? ")

class Computer(Player_BASE):
    pass



if __name__ == "__name__":
    player1 = Player()
    player2 = Computer()
    player1.create()
    player2.create()

    print(player1.name)
    print(player2.name)
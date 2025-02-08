class Character:
    def __init__(self, name):
        self.name = name
        self.stamina = 100
        self.coins = 0
        self.dexterity = 100
    
    def __str__(self):
        return f"Name: {self.name} Stamina: {self.stamina} Coins: {self.coins} Dexterity: {self.dexterity}"

eragon = Character("Eragon")
saphira = Character("Saphira")

my_characters = [eragon, saphira]
print(my_characters)
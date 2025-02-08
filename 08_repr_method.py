class Character:
    def __init__(self, name):
        self.name = name
        self.stamina = 100
        self.coins = 0
        self.dexterity = 100
    
    def __str__(self):
        return f"Name: {self.name} Stamina: {self.stamina} Coins: {self.coins} Dexterity: {self.dexterity}"

    def __repr__(self):
        return self.name

eragon = Character("Eragon")
saphira = Character("Saphira")
brom = Character("Brom")
galbatorix = Character("Galbatorix")
orik = Character("Orik")
roran = Character("Roran")

my_characters = [eragon, saphira, brom, galbatorix, orik, roran]
print(my_characters[-1])
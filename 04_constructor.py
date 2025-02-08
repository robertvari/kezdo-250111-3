class Character:
    # the constructor
    def __init__(self, name, age, coin=0):
        # self.name is a instance attribute
        self.name = name
        self.age = age
        self.coin = coin

eragon = Character("Eragon", 23, 100)
saphira = Character("Saphira", 12, 0)

print(eragon.name, eragon.age, eragon.coin)
print(saphira.name, saphira.age, saphira.coin)
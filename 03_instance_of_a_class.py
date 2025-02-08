class Character:
    # class attributes
    name = None
    age = 0
    inventory = []
    coins = 0
    strength = 100

# Make an instance of the Character class
eragon = Character()
saphira = Character()

# Give names to your characters
eragon.name = "Eragon"
eragon.age = 23
eragon.coins = 120
eragon.inventory = ["Bread", "Sword"]

saphira.name = "Saphira"
saphira.age = 10

print(eragon.name, eragon.age, eragon.coins, eragon.inventory)
print(saphira.name, saphira.age)
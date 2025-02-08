class Character:
    # class attribute
    book_series = "Eragon"

    def __init__(self, name):
        # instance attribute
        self.name = name

saphira = Character("Saphira")
brom = Character("Brom")

print(saphira.name, saphira.book_series)
print(brom.name, brom.book_series)

Character.book_series = "Star Wars"

print(saphira.name, saphira.book_series)
print(brom.name, brom.book_series)
class Character:
    def __init__(self, name):
        # public attribute
        self.name = name

        # protected attribute
        self._name = name

        # private attribute
        self.__name = name

    def __str__(self):
        return self.__name

eragon = Character("Eragon")

print(eragon.__name)
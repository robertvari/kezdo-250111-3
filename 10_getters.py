class Character:
    def __init__(self, name):
        # private attribute
        self.__name = name
        self.__coins = 100
    
    def get_name(self):
        return self.__name
    
    def get_coins(self):
        return self.__coins

eragon = Character("Eragon")
print(eragon.get_coins())
class Character:
    def __init__(self, name):
        # private attribute
        self.__name = name
        self.__coins = 100
    
    @property
    def name(self):
        return self.__name
    
    @property
    def coins(self):
        return self.__coins
    
    @coins.setter
    def coins(self, new_coins):
        assert isinstance(new_coins, int), "set_coins accepts integers only"
        assert new_coins > 0, "Coins must be greater than 0"
        self.__coins = new_coins

eragon = Character("Eragon")
eragon.coins = "Robert"
print(eragon.name, eragon.coins)
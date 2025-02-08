class Character:
    def __init__(self, name):
        # private attribute
        self.__name = name
        self.__coins = 100
    
    def get_name(self):
        return self.__name
    
    def get_coins(self):
        return self.__coins
    
    def set_coins(self, new_coins):
        assert isinstance(new_coins, int), "set_coins accepts integers only"
        assert new_coins > 0, "Coins must be greater than 0"
        
        self.__coins = new_coins

eragon = Character("Eragon")
print(eragon.get_coins())
eragon.set_coins(10)
print(eragon.get_coins())
class Card:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value
    
    @property
    def name(self):
        return self.__name
    
    @property
    def value(self):
        return self.__value

    def change_ace_value(self):
        if self.__value == 11:
            self.__value = 1

    def __str__(self):
        return f"Name: {self.__name} Value: {self.__value}"
    
    def __repr__(self):
        return self.__name
    

if __name__ == "__main__":
    card1 = Card("Diamond Ace", 11)
    card2 = Card("Diamond 2", 2)
    card2.change_ace_value()

    hand = [card1, card2]
    print(card2)
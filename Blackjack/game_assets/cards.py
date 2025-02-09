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


class Deck:
    def __init__(self):
        self.__cards = []
    
    def create(self):
        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        suits = ["Heart", "Club", "Diamond", "Spade"]
    
    def __str__(self):
        return f"{self.__cards}"

if __name__ == "__main__":
    deck = Deck()
    print(deck)
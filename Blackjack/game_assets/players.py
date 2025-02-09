import random, time

class Player_BASE:
    def __init__(self):
        self.__name = None
        self.__credits = 0
        self.__hand = []
        self.__playing = True

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def hand_value(self):
        return sum([card.value for card in self.__hand])

    @property
    def playing(self):
        return self.__playing
    
    @playing.setter
    def playing(self, new_value):
        self.__playing = new_value

    def create(self):
        self.__credits = random.randint(10, 100)
        self.__name = self.__get_random_name()

    def draw(self, deck):
        while self.__playing:
            if self.hand_value <= random.randint(16, 19):
                print(f"{self.__name} draws a card")
                time.sleep(2)
                new_card = deck.draw()
                if self.hand_value > 10 and new_card.value == 11:
                    new_card.change_ace_value()
                self.__hand.append(new_card)
            else:
                print(f"{self.__name} finishes drawing.")
                self.__playing = False

    def init_hand(self, deck):
        self.__hand.clear()
        self.__playing = True

        new_card = deck.draw()
        self.__hand.append(new_card)

        new_card = deck.draw()
        if self.hand_value > 10 and new_card.value == 11:
            new_card.change_ace_value()
        self.__hand.append(new_card)

    def show_hand(self):
        print(f"{self.__hand} Hand value: {self.hand_value}")

    def add_card(self, new_card):
        if self.hand_value > 10 and new_card.value == 11:
            new_card.change_ace_value()
        self.__hand.append(new_card)

    def __get_random_name(self):
        first_names = ["Liam", "Emma", "Noah", "Olivia", "Ethan", "Ava", "James", "Sophia", "Benjamin", "Mia"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def __str__(self):
        return f"Name: {self.__name} Credits: {self.__credits}"

class Player(Player_BASE):
    def create(self):
        super().create()
        self.name = "Robert Vari"
    
    # if we override a method the signature has to match!!!!!
    def draw(self, deck):
        print(f"This is your turn {self.name}")
        while self.playing:
            if self.hand_value > 21:
                print("Your hand value is greater than 21")
                self.playing = False
                break

            self.show_hand()

            respons = input("Do you want to draw a new card? (y/n)")
            if respons == "y":
                new_card = deck.draw()
                print(f"Your new card: {new_card}")
                self.add_card(new_card)
            else:
                self.playing = False


class Computer(Player_BASE):
    pass



if __name__ == "__main__":
    from cards import Deck

    player1 = Player()
    player2 = Computer()
    player1.create()
    player2.create()

    deck = Deck()

    # start new round and drow two cards for each player
    player1.init_hand(deck)
    player2.init_hand(deck)

    # each player starts their round
    player1.draw(deck)
    player2.draw(deck)

    # show hand to decite who wins
    player1.show_hand()
    player2.show_hand()
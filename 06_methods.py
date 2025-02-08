class Character:
    def __init__(self, name):
        self.name = name

    # this is a method (a classic python function with a self)
    def say_hello(self):
        print(f"Hello, my name is {self.name}")
    
    def how_are_you(self):
        print("I'm fine. And you?")

eragon = Character("Eragon")
saphira = Character("Saphira")

eragon.say_hello()
saphira.say_hello()

eragon.how_are_you()
import ninjas

class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health= health
        self.energy = energy

    def sleep(self):
        print(f'{self.name} is sleeping.')
        self.energy += 25

    def eat(self):
        print(f'{self.name} is eating.')
        self.energy += 5
        self.health += 10

    def play(self):
        print(f'{self.name} is playing.')
        self.health += 5

    def noise(self):
        print(f'{self.name} is making a pet sound.')



steve = Ninja('Steven', 'Segal', Pet('Sparky', 'dog', 'sit', 10, 10), 10, 10)
sparky = Pet('Sparky', 'dog', 'sit', 10, 10)


steve.feed(Pet)
steve.walk(Pet)
steve.bathe(Pet)

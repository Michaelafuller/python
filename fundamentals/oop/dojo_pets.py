class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self, pet):
        print(f'{self.first_name} is walking their pet.')
        self.pet.play()
        return self
    
    def feed(self, pet):
        print(f'{self.first_name} feeds their pet.')
        self.pet.eat()
        return self


    def bathe(self, pet):
        print(f'{self.first_name} is bathing their pet.')
        self.pet.noise()
        return self

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
        return self

    def eat(self):
        print(f'{self.name} is eating.')
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        print(f'{self.name} is playing.')
        self.health += 5
        return self

    def noise(self):
        print(f'{self.name} is making a pet sound.')
        return self

steve = Ninja('Steven', 'Segal', Pet('Sparky', 'dog', 'sit', 10, 10), 10, 10)


steve.feed(Pet).walk(Pet).bathe(Pet)

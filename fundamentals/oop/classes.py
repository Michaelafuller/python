import random

class Game:
    players = []
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        Game.players.append(self)
        is_fighting = False

    def battle(self):
        is_fighting = True
        turn = 0
        while(is_fighting):
            if self.p1.health <= 0 or self.p2.health <= 0:
                self.is_fighting = False

            if turn % 2 == 0:
                self.p1.attack(self.p2)
            else:
                self.p2.attack(self.p1)

    @classmethod
    def show_players(cls):
        for player in cls.players:
            print(player.name)
        return cls

class Character:
    def __init__(self, name, health=100, strength=70, defense=50, ac=10, skill=10):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.ac = ac
        self.skill = skill

    def info(self):
        print(self.name)
        print(self.health)
        print(self.strength)
        print(self.defense)

    def changeHealth (self, amount):
        self.health += amount

    def attack(self, target):
        attack_roll = random.randint(1,20)
        print(f'{self.name} rolled a {attack_roll} attack roll.')

        if attack_roll > target.ac:
            print(f'{self.name} attacks {target.name}')
            target.block(self)

        else:
            print(f'{self.name} missed big time!')
        return self

    def block(self, attacker):
        block_roll = random.randint(1,20)
        if block_roll < self.skill:
            print(f'{self.name} counter attacks {attacker}.')
            self.attack(attacker)


class Human(Character):
    def __init__(self, name, health=120, strength=50, defense=50, ac=12, skill=10):
        super().__init__(name, health, strength, defense, ac, skill)
    
    def info(self):
        print('I am a human')
        super().info()

class Dwarf(Character):
    def __init__(self, name, health=150, strength=70, defense=30, ac=13, skill=10):
        super().__init__(name, health, strength, defense, ac, skill)
    

class Halfling(Character):
    def __init__(self, name, health=60, strength=40, defense=70, ac=9, skill=10):
        super().__init__(name, health, strength, defense, ac, skill)
    


anthony = Human('Anthony')
dylan = Halfling('Dylan')

anthony.attack(dylan)
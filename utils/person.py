import random
class Person:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def atack(self, other):
        other.hp -= self.damage

    def alive(self):
        return self.hp > 0

class Hero(Person):
    rasas = ['Единорог', "Панда"]
    def __init__(self, name, rasa, hp, damage):
        super().__init__(name, hp, damage)
        self.rasa = rasa
        self.lvl = 1
        self.xp = 0

    @staticmethod
    def create_hero(name, rasa):
        hp = random.randint(30, 60)
        damage = random.randint(30, 60)
        return Evil(name, rasa, hp, damage)

    def run(self, other):
        way = random.randint(0, 1)
        if way:
            other.atack(self)
        return way


    def check_lvl(self, maxxp):
        if self.xp > maxxp:
            self.lvl += 1
            self.xp = 0

    def get_surprise(self):
        health = {5: 'food'}
        power = {10: 'weapon'}
        ch = random.randint(0, 1)
        if ch:
            des = random.choice(list(health.keys()))
            self.hp += des
            return des, health[des]
        else:
            des = random.choice(list(power.keys()))
            self.hp += des
            return des, power[des]

    def __str__(self):
        return f'Hero({self.name}, {self.rasa}, {self.hp}, {self.damage})'

class Evil(Person):
    @staticmethod
    def create_evil(hero):
        name = random.choice(['Яга', "Кощей"])
        hp = random.randint(30, 60 ) * hero.lvl * 0.5
        damage = random.randint(30, 60) * hero.lvl * 0.5
        return Evil(name, hp, damage)



hero1 = Hero('kfs', 'sdaf', 1, 1)
ev1 = Evil.create_evil(hero1)
print(hero1.hp)
print(hero1.run(ev1))
print(hero1.hp)

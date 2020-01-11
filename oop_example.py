import random

class Animal:
    def __init__(self):
        self.k = 1
    def fressen(self, food_mass):
        self.weight = self.weight + food_mass * self.k

class Panda(Animal):
    all_pandas = []
    def __init__(self, name):
        Animal.k = 0.5
        self.nom = str(name)
        self.weight = 1
        Panda.all_pandas.append(self.nom)
        print("New Panda "+ self.nom)

    def __str__(self):
        return "This is a Panda called " + self.nom + ", and its weight is " + str(self.weight) + "kg"

class Koala(Animal):
    def __init__(self, name):
        Animal.k = 0.25
        self.name = str(name) 
        self.weight = 0.2
        print("New Koala "+ self.name+ " was born")

class Snake(Animal):
    def __init__(self, given_name):
        Animal.k = 0.1
        self.name = given_name
        self.weight = (random.random() + 1)/2 * 3.14

    def __str__(self):
        s = "="
        s = s*int(self.weight*10)
        return self.name+"  <<"+s+"§--´"

pipi = Snake("PiPi")
pibi = Snake("PiBi")
print(pipi)
pipi.fressen(3)
print(pipi)


koala_1 = Koala("Koala 1")
print(koala_1.weight)
koala_2 = Koala("Koala 2")
koala_1.fressen(0.1)
print(koala_1.weight)


a = Panda("Lu")
b = Panda("Qu")
c = Panda(3.14)
print(c)
print(a)
a.fressen(0.5)
a.fressen(1)
print(a)


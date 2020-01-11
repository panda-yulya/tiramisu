class Panda:
    all_pandas = []
    def __init__(self, name):
        self.nom = str(name)
        self.weight = 1
        Panda.all_pandas.append(self.nom)
        print("New Panda "+ self.nom)

    def fressen(self, food_mass):
        self.weight = self.weight + food_mass/2

    def __str__(self):
        return "This is a Panda called " + self.nom + ", and its weight is " + str(self.weight) + "kg"

class Koala:
    def __init__(self, name):
        self.name = str(name) 
        self.weight = 0.2
        print("New Koala "+ self.name+ " was born")
    
    def fressen(self, food_mass):
        self.weight = self.weight + food_mass/4

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


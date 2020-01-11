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

a = Panda("Lu")
b = Panda("Qu")
c = Panda(3.14)
print(c)
print(a)
a.fressen(0.5)
a.fressen(1)
print(a)
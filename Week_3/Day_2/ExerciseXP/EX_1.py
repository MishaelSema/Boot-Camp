class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Siamese(Cat):
    pass
cat1=Bengal("minu",4)
cat2=Chartreux("minet",2)
cat3=Siamese("scott",6)
all_cats=[cat1,cat2,cat3]
sarah_pet=Pets(all_cats)

sarah_pet.walk()



class farm():
    def __init__(self,name):
        self.name=name
        self.animal=[]
        self.animal_names=[]
    def add_animals(self,animal_name,number=1):
        if number==1:
            num_animal=animal_name
        else:
            num_animal=(animal_name + ",") * (number-1) + animal_name
            num_animal=num_animal.split(",")
        if num_animal==animal_name:
            self.animal.append(animal_name)
        else:
            for i in num_animal:
                self.animal.append(i)
        print(f"{number} {animal_name}(s) has(have) been added to the farm")
    def get_info(self):
        print(f"{self.name}'s farm\n")
        
        for i in self.animal:
            if i not in self.animal_names:
                self.animal_names.append(i)
        for j in self.animal_names:
            print(f" {j} : {self.animal.count(j)}\n")
            continue
        print("    E-I-E-I-O")
    def get_animal_type(self):
        return sorted(self.animal_names)
    def get_short_info(self):
        for i in self.animal_names :
            print(f"{self.name} has {i}s")
md=farm("McDonald")
md.add_animals("pig",4)
md.add_animals("Horse",5)
md.add_animals("Donkey",2)
md.get_info()
md.get_animal_type()
md.get_short_info()
print(md.animal)
class zoo():
    def __init__(self,zoo_name):
        self.animals=[]
        self.sorted_animals={}
        sorted(self.animals)
        self.name=zoo_name
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"Added! {new_animal} to the zoo")
        else:
            print(f"{new_animal} is already in the zoo")
    def get_animals(self):
        print(f"The animals at {self.name.capitalize()} zoo: ")
        for i in self.animals:
            print(i)
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animal.remove(animal_sold)
            print(f"Sold {animal_sold} from zoo")
        else:
            print(f"{self.name} Zoo does not have an animal named {animal_sold}")
    def sort_animals(self):
        
        for animal in self.animals:
            first_letter = animal[0]
            if first_letter not in self.sorted_animals:
                self.sorted_animals[first_letter] = []
            self.sorted_animals[first_letter].append(animal)
            continue
        for key, value in self.sorted_animals.items():
            if len(value) == 1:
                self.sorted_animals[key] = value[0]
        print(self.sorted_animals)
    def get_groups(self):
        for key,values in self.sorted_animals.items():
            print(f"Animals in group {key} are: \n"f"{values}")
    def ramat_gan_safari(self): 
        self.add_animal('Pig')
        self.add_animal("Puma")
        self.add_animal("Horse")
        self.add_animal("Elephant")
        self.add_animal("Antelope")
        self.get_animals()
        self.sort_animals()
        self.get_groups()
zoo1=zoo("vogt")
zoo1.ramat_gan_safari()

 


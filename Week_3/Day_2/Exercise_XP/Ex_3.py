from EX_2 import Dog
import random
class PetDog(Dog):
    def __init__(self, name, age, weight,trained=False):
        super().__init__(name, age, weight)
        self.trained=trained
    def train(self):
        Dog.bark()
        self.trained=True
    def play(self,*dogs):
        print(f"{dogs} all play together")
    def do_a_trick(self):
        tricks=[f"{self.name} does a barrel roll.",
            f"{self.name} stands on his back legs.",
            f"{self.name} shakes your hand.",
            f"{self.name} plays dead."]
        if self.trained==True:
            print(random.choice(tricks))
dog_1=PetDog("zabu",3,19,True)
dog_1.do_a_trick()
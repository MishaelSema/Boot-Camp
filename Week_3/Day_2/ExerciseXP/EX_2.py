class Dog():
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    def bark(self):
        print(f"{self.name} is barking!!")
    def run_speed(self):
        run_spd=self.weight/self.age*10
        return run_spd
    def fight(self,other_dog):
        print(f"~`~`~`~{self.name} VS {other_dog.name}~`~`~`~")
        if self.run_speed()*self.weight > other_dog.run_speed()*other_dog.weight:
            print(f"===>{self.name} WON the FIGHT!!!\n")
        elif self.run_speed()*self.weight < other_dog.run_speed()*other_dog.weight: 
            print(f"===>{other_dog.name} WON the FIGHT!!!\n")
        else:
            print(f"Its a tie!!")
dog1=Dog("Rocky",4,20)
dog2=Dog("Lion",6,13)
dog3=Dog("Zabra",3,25)
#dog1.fight(dog2)
#dog1.fight(dog3)
#dog2.fight(dog3)
#dog1.bark()
#dog1.bark()
#dog2.bark()
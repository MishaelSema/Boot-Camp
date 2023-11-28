class dog():
    def __init__(self,name,height):
        self.name=name
        self.height=height
        print("--------NEW DOG INITIALIZED!!!--------")
    def bark(self):
        print(f"{self.name} goes wouf!")
    def jump(self):
        print(f"{self.name} jumps {self.height*2}cm high!")
davids_dog=dog("Rex",50)
print(f"{davids_dog.name} is {davids_dog.height}cm tall")
davids_dog.bark()
davids_dog.jump()
sarahs_dog=dog("Teacup",20)
print(f"{sarahs_dog.name} is {sarahs_dog.height}cm tall")
sarahs_dog.bark()
sarahs_dog.jump()
if davids_dog.height>sarahs_dog.height:
    print(f"{davids_dog.name} is the BIGGER Dog")
elif sarahs_dog.height>davids_dog.height:
    print(f"{sarahs_dog.name} is the BIGGER Dog")

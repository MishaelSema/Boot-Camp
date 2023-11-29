class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family for the new born child!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name and member['age'] >= 18:
                return True
        return False

    def family_presentation(self):
        print(f"The {self.last_name} family:")
        for member in self.members:
            print(f"{member['name']}")


initial_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]


family = Family('Johnson', initial_members)
family.born(name='Emily', age=0, gender='Female', is_child=True) 
print(family.is_18('Michael'))
family.family_presentation()

#EXERCISE_2
class TheIncredibles(Family):

    
    def __init__(self, last_name,members):
        Family.__init__(self,last_name,members)

    def use_power(self, name):
        member = [member for member in self.members if member["name"] == name][0]
        if member["age"] > 18:
            print(f"{member['name']} uses {member['power']}")
        elif member["age"] < 18:    
            raise Exception("Member is not over 18 years old")
        

    def incredible_presentation(self):
        Family.family_presentation(self)
        for member in self.members:
            print(f"{member['incredible_name']} - {member['power']}")

ini_members=[
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]

family = TheIncredibles("Incredible",ini_members)
family.incredible_presentation()

family.born(name="Baby Jack", age=0, gender="Male", is_child=True, power="Unknown Power",incredible_name= "Jack")

family.incredible_presentation()

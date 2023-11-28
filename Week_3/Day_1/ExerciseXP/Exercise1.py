class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
cat_1=Cat("Scott",4)
cat_2=Cat("Natalie",2)
cat_3=Cat("Kitty",5)
def oldest_cat():
    if cat_1.age>cat_2.age and cat_1.age>cat_3.age:
        return cat_1
    elif cat_2.age>cat_1.age and cat_2.age>cat_3.age:
        return cat_2
    else:
        return cat_3
print(f"the oldest cat is {oldest_cat().name} and is {oldest_cat().age} years old")
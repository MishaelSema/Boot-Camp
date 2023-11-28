class Door():
    def __init__(self,is_opened):
        self.open=is_opened
    def open_door(self):
            print("DOOR IS OPEN")
    def close_door(self):
        print("DOOR IS CLOSE")
class BlockedDoor(Door):
    
    def open_door(self):
        print("a blocked door cannot be opened or closed")
    def close_door(self):
        print("a blocked door cannot be opened or closed")
my_door=Door(True)
my_door.open_door()


class Computer():

    def __init__(self):
        self.name = "Apple Computer" # public
        self.__max_price = 900 # private

    def sell(self):            # public method
        print(f"Selling Price: {self.__max_price}")

    def __sell(self):          # private method
      print('This is private method')

    def set_max_price(self, price):
        self.__max_price = price

c = Computer()
c.set_max_price(100)

c.sell()
class Alien():
    def __init__(self, name, planet):
        self.name = name
        self.planet = planet

    def fly(self):
        print(self.name, 'is flying!')

    def sleep(self):
        print("Aliens don't sleep")

class Animal():
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print("zzzZZZZZ")

class Dog(Animal):
    def bark(self):
        print("{} barked, WAF !".format(self.name))

class AlienDog(Alien, Dog):
    def bark(self):
        print("{} barked, 0ul10ul0u (that's how aliens dogs bark..) !".format(self.name))


my_normal_dog = Dog("Roger")
my_normal_dog.sleep()
# >> zzzZZZZZ

my_normal_dog.bark()
# >> Roger barked, WAF !

my_alien_dog = AlienDog("Rex", "Neptune")
print(my_alien_dog.planet)
# >> Neptune

my_alien_dog.fly()
# >> Rex is flying!

my_alien_dog.sleep()
# >> Aliens don't sleep

my_alien_dog.bark()
# >> Rex barked, 0ul10ul0u (that's how aliens dogs bark..) !


class A():

    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C():
    def dothis(self):
        print("doing this in C")


class D(B, C):
    pass

d_instance = D()
d_instance.dothis()



class Book():
    def __init__(self, title, author, publication_date, price):
        self.title = title
        self.author = author
        self.publication = publication_date
        self.price = price

    def present(self):
        print(f'Title: {self.title}')

class Fiction(Book):
    def __init__(self, title, author, publication_date, price, is_awesome):
        super().__init__(title, author, publication_date, price)
        self.genre = 'Fiction'
        self.is_awesome = is_awesome
        if self.is_awesome:
            self.bored = False
            print('Woow this is an awesome book')
        else:
            self.bored = True
            print('I am very bored')

if __name__ == '__main__':
    foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
    foundation.present()
    print(foundation.price)
    print(foundation.bored)
    boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
    print(boring_book.bored)




my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
def sum_num(lists):
    add=0
    for i in lists:
        try:
            add+=i
            print(add)
        except:
            print("addition of intergers and other data types not possible")
    
sum_num(my_list)
        
    
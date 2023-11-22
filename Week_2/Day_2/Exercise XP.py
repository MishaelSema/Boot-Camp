#Ex_1
my_fav_numbers = {1, 2, 3, 4, 5}
my_fav_numbers.add(6)
my_fav_numbers.add(7)
my_fav_numbers=set(list(my_fav_numbers)[:-1])
friend_fav_numbers = {8, 9, 10}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("EX_1: ","my_fav_numbers:", my_fav_numbers)
print("EX_1: ","friend_fav_numbers:", friend_fav_numbers)
print("EX_1: ","our_fav_numbers:", our_fav_numbers)
#Ex_2
my_tuple=(1,2,3,4)
y=list(my_tuple)
y.append(5)
my_tuple=tuple(y)
print("EX_2: ",my_tuple)
#Ex_3
basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket.remove("Banana")
basket.remove("Blueberries")
basket.insert(len(basket),"Kiwi")
basket.insert(0,"Apples")
print("EX_5: ","there is(are)", basket.count("Apples"),"Apples in the basket")
basket.clear()
print("EX_3: ",basket)
#Ex_4
#a float is a rational or decimal number.
#an interger is all positive and negative whole numbers while float are fraction numbers
b=1
my_list=[]
while len(my_list)<8:
    b=b+0.5
    my_list.append(b)
    b=b
print("EX_4: ",my_list)
#Ex_5
a=0
my_list=[]
for i in range(1,21):
    a+=1
    my_list.append(a)
    a=a
print("EX_5: ",my_list) 
#Ex_5
a=0
my_list=[]
new_list=[]
for i in range(1,21):
    a+=1
    my_list.append(a)
    a=a
for j in my_list:
    if my_list.index(j) % 2 ==0:
        new_list.append(j) 
print("EX_5: ",new_list) 
#EX_6
your_name="Mishael"
while input("What is my name: ") != your_name:
    continue
#Ex_7
fav_fruit=input("what is(are) yoour favorite fruit(s). Seperate them with space.\n FRUIT NAME: ")
fav_list=fav_fruit.split(" ")
if input("Name any fruit: ") in fav_list:
    print("Ex_7: ","You chose one of your favorite fruits! Enjoy!")
else:
    print("Ex_7: ","You chose a new fruit. Hope you enjoy")
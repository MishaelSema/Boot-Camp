# Initialize list
list1 = [5, 10, 15, 20, 12, 50, 23]
list1=(sorted(list1))
if 20 in list1:
    a=list1.index(20)
    print(a)
    list1.insert(a+1, 21)
    print(list1)
else:
    print("12 aint here")
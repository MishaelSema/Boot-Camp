string=input('Write a String')
if len(string)<10:
    print('string is too short')
elif len(string)>10:
    print('string is too long')
elif len(string)==10:
    print('perfect string')
    print(string[0],string[-1])


list=[1,2,3,4,5,6]
for i in list:
    if list[i]==8:
        print('found')
    else:
        print('not found')

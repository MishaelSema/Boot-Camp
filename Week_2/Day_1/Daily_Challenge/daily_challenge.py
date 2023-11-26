string=input('Write a String')
if len(string)<10:
    print('string is too short')
elif len(string)>10:
    print('string is too long')
elif len(string)==10:
    print('perfect string')
    print(string[0],string[-1])
for i in range(len(string)):
    print(string[:i+1])
    



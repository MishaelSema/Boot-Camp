print("Hello World!\n"*5)

computer_brand='Lenovo'
print("I have a "+computer_brand+" computer")

name='Mishael'
age='18'
shoe_size='43'
info='My name is '+ name +' and i am '+age +' years old. I love playing basketball and my shoe size is '+ shoe_size+'.'
print(info)


a=13
b=5
if a>b:
    print('Hello World')

    
    number=input('write any number')
    if int(number) % 2 == 1:
        print(number+' is and odd number')
    else:
        print(number+' is an even number')

my_name='Mishael'
your_name=input('Hey!, what is your name')
if my_name==your_name:
    print('Wow, twin huh')
else:
    print('sorry, we cant share the bread')

your_height=input('What is your heigth in inches')
if float(your_height)*2.54 >= 145:
        print('ALRIGHT!!!, proceed to your ride')
else:
     print('Too Bad. Come back when you are taller')
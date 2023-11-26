names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name=input("write your name: ")
for i in names:
    if i==name:
        print(names.index(i))

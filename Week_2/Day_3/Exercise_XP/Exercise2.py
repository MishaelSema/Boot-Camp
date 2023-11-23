family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total=0
family[input("what is your name: ")]=int(input("what is your age: "))
for k,v in family.items():
    if v<3:
        cost=0
    if v in range(3,13):
        cost=10
    if v>12:
        cost=15
    total+=cost
    print(f"{k} will pay ${cost}")
    
print(f"total cost is: ${total}")




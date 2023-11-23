import random
def randomizer():
    int=input("Enter any number between 1 and 100: ")
    rand=random.randrange(1,101)
    if rand==int:
        print("You won")
    else:
        print("You failed\n"f"Your number {int}\n"f"Gold number {rand}")
randomizer()
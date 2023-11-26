import random
def get_random_temp(season):
    if season == "Winter":
        ran=float(random.randrange(-10,16))
    elif season == "Spring":
        ran=float(random.randrange(16,20))
    elif season == "Autumn":
        ran=float(random.randrange(20,28))
    elif season == "Summer":
        ran=float(random.randrange(28,41))
    return ran
def main():
    season=input("Write any season: ")
    ran_temp=get_random_temp(season)
    print(f"The temperature right now is {ran_temp}°C")
    if ran_temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif ran_temp in range(0,16):
        print("Quite chilly! Don’t forget your coat")
    elif ran_temp in range(16,24):
        print("What a nice warm day")
    elif ran_temp in range(24,32):
        print("Its hot outside")
    elif ran_temp in range(32,41):
        print("shhhhh, too hot")
main()
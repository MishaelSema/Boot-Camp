month=int(input("Write a month(in digits): "))
if month in range(3,6):
    print("it is SPRING")
elif month in range(6,9):
    print("it is SUMMER")
elif month in range(9,12):
    print("it is AUTUMN")
elif month == 12 or 1 or 2:
    print("it is WINTER")
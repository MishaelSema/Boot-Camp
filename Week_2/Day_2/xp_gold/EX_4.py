val=input("Write 3 numbers: ")
values=val.split(",")
values=[int(i)for i in values]
x=sorted(values)
print(f"The greatest number is: {x[-1]}")
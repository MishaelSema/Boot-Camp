list_1=[]
list_2=[]
for i in range(1500,2501):
    if i%5==0:
        list_1.append(i)
    if i%7==0:
        list_2.append(i)
print("Multiples of 5: ",list_1)    
print("Multiples of 7: ",list_2)
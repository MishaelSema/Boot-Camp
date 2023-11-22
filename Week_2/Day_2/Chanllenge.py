#challenge_1
length=int(input("Enter a length: "))
number=int(input("Enter a number: "))
lists=[]
for i in range(1,length+1):
    lists.append(number*i)
print(lists)
#challenge_2
word=input("Write a word: ")
result = "".join(dict.fromkeys(word))
print(result)
sent=input("write a long sentence without using 'A' ")
while True:
    if "A" in sent:
        sent=input("write a long sentence without using 'A' ")
        continue
    else:
        print("SUCCESS")
        break

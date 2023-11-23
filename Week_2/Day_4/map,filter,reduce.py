people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
names=list(filter(lambda s:len(s)<=4 ,people))
name=list(map(lambda s:f"Hello {s}" ,names))
print(name)
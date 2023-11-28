animals = ["Ape", "Baboon", "Bear", "Cat", "Cougar", "Eel", "Emu"]

def sort_animals(animals):
    sorted_animals = {}
    for animal in animals:
        first_letter = animal[0]
        if first_letter not in sorted_animals:
            sorted_animals[first_letter] = []
        sorted_animals[first_letter].append(animal)

    for key, value in sorted_animals.items():
        if len(value) == 1:
            sorted_animals[key] = value[0]
    return sorted_animals

sorted_animals = sort_animals(animals)
print(sorted_animals)
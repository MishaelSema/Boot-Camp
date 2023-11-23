magician_names=['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magician():
    iter=map(lambda s: s,magician_names)
    print(list(iter))

def make_great():
    iter=map(lambda s: magician_names.append(f"The Great {s}"),magician_names)
    print(list(iter))
make_great()
show_magician()

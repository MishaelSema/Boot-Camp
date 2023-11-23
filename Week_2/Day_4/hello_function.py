def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') 
print(musician)
def say_hello():
    name=input("Whats ur name hommie?")
    if int(input("what is your age?"))<18:
        print(f"Hello! {name}. Your are too young to be on such a site u know ^_^") 
    else:
        print(f"Hello! {name}. Welcome to the club G. Grab ur armmo and load up ~~~~")
say_hello()

def hello(name):
    print(f"Wagwan {name}")

hello("dumbass")

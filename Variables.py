"""
Python Variables:

Variables is a way to store values that can be used later in the program.
The process of having a variable would be declaration, assignment, and use
"""
# Creating Variables
isInteger = 7
name = "John"

# Variable Naming:
    # Legal Naming:
        # 1. A variable name must start with a letter or the underscore character
        # 2. A variable name cannot start with a number
        # 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
        # 4. Variable names are case-sensitive
        # Ex:
            # myvar = "John"
            # my_var = "John"
            # _my_var = "John"
            # myVar = "John"
            # MYVAR = "John"
            # myvar2 = "John"
    # Illegal Naming
        # 1. If your variable name doesn't follow any of the rules listed previously than it would be considered as an illegal name
        # Ex:
            # 2myvar = "John"
            # my-var = "John"
            # my var = "John"

# Assign Values to Multiple Variables
a , b , c = "Bob" , "Billy" , "Joe"

# Assigning the Same Value to Multiple Variables
d = e = f = "Mama"

# Output Variables
print("My name is " + f)
print(name + e)

# Global Variables
chocolateManufacturers = ["Ferrero Rocher" , "Ghirardelli" , "Toblerone" , "Cadbury" , "Mars" , "Godiva"]
def BodyWash():
    global bodyWashChoice
    bodyWashChoice = ("Axe" , "Dove")

# Local Variables
def Pokemon():
    pokemonSelection = {"Greninja"}
    print(pokemonSelection)

# Non-Local Variables
def PokemonLove():
    def PikachuILoveU():
        nonlocal pikachu
        pikachu = "Pikachu"        
    print(pikachu)

BodyWash()
Pokemon()
PokemonLove()
"""
Tuples:

A Python collection which can't be changed but it is ordered.
This includes trying to changing the Tuple's Values by Adding or Deleting Items won't work.
Allows to have duplicate items.
"""

# Creating a Tuple
playToys = ("Spike", "Crow", "Leon", "Rosa", "Shelly", "Piper") # Use Parantheses when declaring a Tuple
clashToys = ("Witch" , "Golem" , "Giant" , "Archers" , "Wizard" , "Ballon" , "Wall Breakers") # Use Parantheses when declaring a Tuple
games = tuple(("Counter-Strike: Global Strike" , "Rainbow Six Siege" , "Fornite" , "Apex Lgends" , "PlayerUnknown's Battlegrounds" , "Call of Duty")) # Use Double Parantheses when using the tuple Constructor
gamesM = tuple(("Halo" , "Destiny" , "Forza Horizon" , "Assasin's Creed" , "Rocket League" , "Terraria" , "Minecraft", "Red Redemption")) # Use Double Parantheses when using the tuple Constructor
boys = () # Python Won't recognize this as an Empty Tuple
# girls = tuple(()) An empty tuple is 
shortHairs = ("Panav Kotha" , ) # Make sure if you have one Item and don't use the tuple constructor for a Tuple to have a comma so it won'r be recognized as a String or a Number depending on the Value in the Collection

# Accessing a Tuple (Slicing)
print(playToys) # Prints the Entire Tuple

print(playToys[1])  # Prints the Item that has the Index of 1 (Note: Indexing of a List Starts at 0) 
print(playToys[1 :])  # Prints the Items from the index 1 (Included) to the end of the List (Note: Indexing of a List Starts at 0)  
print(playToys[: 1]) # Prints the Items from the start of the list upto 1 (Non-Included) (Note: Indexing of a List Starts at 0) 
print(playToys[1: 3]) # Prints the Items with the Index 1 (Included) to 3 (Non-Included) (Note: Indexing of a List Starts at 0)

print(clashToys[-1]) # Prints the Last Item in the List (Note: Indexing of a List Starts at 0)
print(clashToys[-4 :]) # Prints the Fourth Last Item in the List (Included) to the End of the List (Note: Indexing of a List Starts at 0)
print(clashToys[: -2]) # Prints All the Items in the List to the Second Last Item (Non-Included) (Note: Indexing of a List Starts at 0) 
print(clashToys[-4: -2]) # Prints the Items from the Fourth Item in the List (Included) to the Second Item in the List (Non-Included)
print(classToys[1 : 5 : 2]) # Prints The Items buts Skips some Items (Ex: [1 : 5 : 2] --> Only Items 2 & 4 will be Printed)

# Adding Items to a Tuple 
# Not Possible, convert the Tuple to a List if you want to

# Removing Items off a Tuple
# Not Possible, convert the Tuple to a List if you want to

# Copying a Tuple
# Your hella retarded if your trying to copy a tuple over to another variable because its immutable, if you need reference the original tuple

# Join Tuples
games + gamesM = allGames # Use the + arithmetic operator

# Length of Tuple
len(clashToys)

# In-Built Methods or Functions
playToys.count("Spike")	# Returns the number of times a specified value occurs in a tuple
clashToys.index("Ballon") # Searches the tuple for a specified value and returns the position of where it was found
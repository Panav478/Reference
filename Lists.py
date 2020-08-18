"""
Lists

A Python collection that is changeable and ordered. 
Allows to have duplicate items.
"""
def NoReason(): # Ignore this, not relavent this is something you will learn in a future lesson
    pass
# Creating a List
friends = ["Abhi Sharma" , "Satvik Thati" , "Kana Zhao" , "Harley Cabanag"] # Use Square Brackets when declaring a List
enemies = ["Jeffrey Kennedy" , "Daksh Bhatia" , "Connor Scott" , "Panav Kotha"] # Use Square Brackets when declaring a List
casuals = list(("William Feng" , "Aaron Lee" , "Faiza Imran" , "James Zheng" , "Tyler Mortimore")) # (Note: Must Use Double Parantheses when Declaring a List Using the list constructor)
classmates = list(("Jackson Dunbar" , "Charlie Gorman" , "Cameron Roper" , "Jason Zhang" , "Adarsh Kumarappan" , "Atharv Jain" , "Nayan Nair")) # (Note: Must Use Double Parantheses when Declaring a List Using the list constructor)
moreFriends = [] # Python Will Recognize this as an Empty List
moreEnemies = [] # Python Will Recognize this as an Empty List
moreCasuals = list(()) # Python Will Recognize this as an Empty List and Use Square Brackets when declaring a List
moreClassmates = list(()) # Python Will Recognize this as an Empty List and Use Square Brackets when declaring a List

# Accessing Items in a List (Slicing) (This gets confusing so text me if you don't get or I missed up this Part)
print(friends) # Prints the Entire List

print(friends[1]) # Prints the Item that has the Index of 1 (Note: Indexing of a List Starts at 0)
print(friends[1:] # Prints the Items from the index 1 (Included) to the end of the List (Note: Indexing of a List Starts at 0)   
print(enemies[:2] # Prints the Items from the start of the list upto 2 (Non-Included) (Note: Indexing of a List Starts at 0) 
print(enemies[1:3]) # Prints the Items with the Index 1 (Included) to 3 (Non-Included) (Note: Indexing of a List Starts at 0)

print(enemies[-2]) # Prints the Second Last Item in the List (Note: Indexing of a List Starts at 0)
print(casuals[-2:]) # Prints the Second Last Item in the List (Included) to the End of the List (Note: Indexing of a List Starts at 0)
print(casuals[:-1]) # Prints All the Items in the List to the Last Item (Non-Included) (Note: Indexing of a List Starts at 0)
print(classmates[-4 : -2]) # Prints the Items from the Fourth Item in the List (Included) to the Second Item in the List (Non-Included)

print(classmates[1 : 5 : 2]) # Prints The Items buts Skips some Items (Ex: [1 : 5 : 2] --> Only Items 2 & 4 will be Printed)
# Adding Items to a List
friends.append("Guru Charan Lingamallu") # The append method helps to add an item to the end of a List
enemies.append("Vishal Tatini") # The append method helps to add an item to the end of a List
casual.insert(2 , "Atharva Kamat") # The insert method helps to add an item and choose where to be placed in the List
classmates.insert(0, "Charlie Jennings") # The insert method helps to add an item and choose where to be placed in the List

# Removing Items off a List
friends.remove("Abhi Sharma") # The remove method removes the specified item mentioned from the List
del enemies[1] # The del keyword removes the item from the List when specifying the index
casuals.pop() # IF the argument given to the pop method will remove the item with the index that was specified otherwise it will remove the last item in the List
classmates.clear() # Clears ALL the Items off the List so now it is an empty list but STILL EXISTENT
# Deleting List
del friends # Deletes the List completely (THE LIST DOES NOT EXIST)

# Copying a List
friends = moreFriends # Now all the items that the List friends contains is now bigFriends BUT WHENEVER EITHER OF THE LISTS IS CHANGED THE OTHER LIST WILL BE AFFECTED
enemies.copy() = moreEnemies # Now all the items that thee List friends contains is now bigFriends BUT WHENEVER EITHER LISTS IS CHANGED THE OTHER WOULD NOT BE AFFECTED
list(casuals) = moreCasuals # Now all the items that thee List friends contains is now bigFriends BUT WHENEVER EITHER LISTS IS CHANGED THE OTHER WOULD NOT BE AFFECTED

# Joining Lists
friends + enemies = close # Concatenate 2 Lists with + Aritmetic Operator
moreFriends.append(moreEnemies) = far # Use the append method to join 2 Lists
casuals.extend(classmates) # Use the extend method to join 2 Lists

# Length of List
len(friends)

# In-Built Functions or Methods
friends.count("Abhi Sharma") # Counts how many times a specific item repeats in the List
friends.index("Abhi Sharma") # Returns the index of the specified value which was provided
friends.reverse() # Reverses the order of the items in the List (Ex. [A , B] --> [B , A])
friends.sorted(reverse = false , key = NoReason)  # Allows you to short Alphabetly along with 2 parameters of reverse and key (reverse switches the order ad key allows you to pass through the list to a function <-- (Don't worry about what that is now)) and doesn't modify the list
friends.sort(reverse = True , key = NoReason) # Allows you to short Alphabetly along with 2 parameters of reverse and key (reverse switches the order ad key allows you to pass through the list to a function <-- (Don't worry about what that is now)) and does modify the list
"""
Sets and Frozensets

A Python collections which are unordered. Share almost the same methods
Does not take duplicate Items.

Sets

Can be changed after declaration.

Frozensets

Is an immutable collection like a Tuple so can't not be changed after declaration.
This includes trying to changing the Tuple's Values by Adding or Deleting Items won't work.
"""

# Creating Sets and Frozensets
firstNames = {"Panav" , "Abhi" , "Satvik"}
lastNames = {"Kotha" , "Sharma" , "Thati"}
publicFigures = set(("Donald Trump" , "Joe Biden" , "Nancy Pelosi" , "Micth McConnell" , "Mike Pence" , "Mike Bloomberg" , "Bernie Sanders"))
rappers = set(("Eminem" , "Lil Uzi Vert" , "Juice Wrld" , "Travis Scott" , "Drake" , "Youngboy" , "Migos"))
indianActors = frozenset({"Sharukh Khan" , "Amir Khan" , "Amitabh Bhachan" , "Salman Khan" , "Hrithvik Roshan" , "Ranveer Singh" , "Ranbir Kapoor"})
typesOfGuns = frozenset({"Pistols" , "SMGs" , "Rifles" , "Shotguns" , "Snipers" , "AK-47s"})
indianCricketPlayers = frozenset({"Virat Kohli" , "Sachin Tendulkar"})
schools = {} # Python won't recognize this as a Set and instead as a Dictionary
colleges = set(()) # Python will be able to recognize as this Empty Set with using the set constructor
bots = frozenset({})

# Accessing Items in Sets and Frozensets
# Accessing Items is Not Possible with a Sets or Frozensets because Both Collection 

# Adding Items with Sets and Frozensets
firstNames.add("Kana") # Adds "Kana" to the List, can only add one item at a time with the add method
lastNames.update(["Zhao" , "Pig"]) # Adds "Zhao" and "Pig" can add multiple items at once
# Adding Items with Frozensets is not possible beacuse it is an immutable collection

# Remove Items with Sets and Frozensets
publicFigures.remove("Joe Biden") # Removes the item "Joe Biden" from the Set but can raise an error if the item does not exist
rappers.discard("Kodak Black") # Removes the item "Kodak Black" and won't raise an error if the item doesn't previously exist in the Set (Note: This method only works for Sets)
rappers.pop() # Removes a random Item off a List because it is UnOrdered
publicFigures.clear() # Clears all the items in the Set publicFigures
# Can not remove Items from a Frozenset because it is an immutable Collection

# Deleting Sets and Frozensets
del publicFigures
del bots

# Copying in Sets and Frozensets
celebraties = publicFigures.copy()
moreTypesofTypes = typesOfGuns.copy()

# Joining Sets and Frozensets
names = firstnames.union(lastnames) # The union method combines both sets into a new set
indianCelebraties.update(indianActors) # Adds all the items in the Set indianActors to indianCelebraties

indianCelebraties = indianActors.union(indianCricketPlayers) # he union method combines both frozensets into a new frozenset


# In-Built Functions and Methods # Satvik I should have used better Sets to make it even more what the method actaully does so feel free to text me if you have any questions
publicFigures.difference(celebraties) # Returns a set containing the difference between two or more sets
publicFigures.difference_update(celebraties) # Removes the items in this set that are also included in another, specified set
publicFigures.intersection(celebraties)	# Returns a set, that is the intersection of two other sets
publicFigures.intersection_update(celebraties) # Removes the items in this set that are not present in other, specified set(s)
publicFigures.isdisjoint(celebraties) # Returns True if there is an intersection between the 2 Sets
publicFigures.issubset(celebraties)	# Returns whether another set contains this set or not
publicFigures.issuperset(celebraties) # Returns whether this set contains another set or not
publicFigures.symmetric_difference(celebraties) # Returns a set with the symmetric differences of two sets
publicFigures.symmetric_difference_update(celebraties) # Inserts the symmetric differences from this set and another
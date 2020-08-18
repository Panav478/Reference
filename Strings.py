"""
Strings

A String is a type of data type in python which is used to represent text.
"""

# Printing a String
print("Hello World!")
print("My name is Panav.")

# Assign a String to a Variable
welcoming = "Hello World"
introduction = "My name is Panav."
name = str("Satvik")
grade = str(9)

# Multi-line Strings
properIntroduction = """Hi. Welcome to Skyline High School.
My name is Panav and I am right now a sophomore here.
Please feel free to contact me if you need any help with anything around school.
Have a great day on the first day of high school."""

# OR with Single Quotes

friends = '''1. Abhi Sharma
2. Satvik Thati
3. Kana Zhao'''

# Slicing/Indexing
print(welcoming[1])
print(welcoming[2 : ])
print(welcoming[2 : 5])

# Negative Indexing
print(welcoming[-1])
print(welcoming[-4 : -1])


# Check String
if "1." in welcoming:
    part = 1.
    print(part)
if "1." not in welcoming:
    part = 1.
    print(part)

# String Concatenation
name = "Bob"
print("My name is " + name)
sentenceStarter = "My name is"
print(sentenceStarter + " " + name + ".")

# String Format
age = 2
sentenceFormat = "My name is Bob and I am {0} years old."
print(sentenceFormat.format(age))
print(sentenceFormat.format(4))
sentenceFunc = "My name is Bob and I am " + str(age) + " years old."
print(sentenceFunc)
sentenceFunc = "My name is Bob and I am " + str(4) + " years old."
print(sentenceFunc)

# Escape Characters
print("You are \"amazing\"") # Allowing Quotations
print("I like \\") # Backslash
print("You are \n amazing") # New Line
print("You are \r amazing") # Carriage Return
print("You are \b amazing") # Backspace
print("You are \f amazing") # Form Feed
print("\171\145") # Octal Value

# Length of String
len(properIntroduction)

# In-Built Functions & Methods (Not Completed --> Work In Progress (Ignore))
friend = "           aBhI sHaRmA"
print(friend.capitalize()) # Capitalizes the first character of the string to upper case
print(friend.casefold()) # Makes all the characters in the string tom lowercase
print(friend.center(100)) # Centers, so you can choose the alignment of the string
print(friend.count("a")) # Counts how many time a certain character occured in the string
print(friend.endswith("rMa")) # Returns a bool value depending on if the string ends with the argument provided
print(friend.find(" ")) # Find if the phrase is present in the string and returns the index, if not present sends a 1
print(friend.index("a")) # Finds the index of the character and returns the index, if not present sends an exception
print(friend.isalnum()) # Returns True if the string contains only alphabets or numbers
print(friend.isalpha()) # Returns True if the string contains only alphabets
print(friend.isdigit()) # Returns True if the string only contains numbers
print(friend.isidentifier()) # Return True if the string follows the same rules used to define a variable
print(friend.islower()) # Returns True if all characters in the string are lower case
print(friend.isnumeric()) # Returns True if all characters in the string are numeric
print(friend.isprintable()) # Returns True if all the character are printable
print(friend.isspace()) # Returns True if there is a space between the string 
print(friend.istitle()) # Returns True if string is a title (1st Word of each Character is captialized)
print(friend.isupper()) # Returns True if all the character are upper case
print(friend.join("Satvik")) # Adds any parameter to end of the string
print(friend.ljust(5)) # Allows you to left adjust the string's position
print(friend.maketrans('a' , "b")) # Replace
print(friend.partition("a")) #
print(friend.replace("hI" , "I")) # Replaces the phrase "hI" to "I" in the String
print(friend.rfind("hI")) #
print(friend.rindex("hI")) #
print(friend.rjust(5)) #
print(friend.rpartition("a")) #
print(friend.) #
print(friend.) #
print(friend.split("a" , 1)) # 1st parameter Splits the string by "a" and the 2nd parameter is the maxsplit
print(friend.) #
print(friend.startswith("    ")) # Returns True if the string starts with what your provided in the parameter
print(friend.strip(" aA")) # Removes any Leading or Trailing Characters in the string
print(friend.title()) # Makes the First Character of Each Word Into UpperCase and anything else LowerCase
print(friend.) #
print(friend.upper()) # Makes ALL characters in the string UpperCase 
print(friend.) #
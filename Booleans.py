"""
Booleans

A data type in Python that allows to have or check for a value as "True" or "False".
"""
# Using Bitwise Operators
print(10 > 9)
print(10 >= 9)
print(10 == 9)
print(10 <= 9)
print(10 < 9)

# IF Statements Check for the Boolean Value In Order to Run
a = 37
b = 420

if a < b:
    print("B made the higher stake.")
elif b < a:
    print("A made the higher stake.")

# Declaration of a Boolean
i = True
j = False
k = bool(1) # All Numbers except 0 is True and any other Data Types (Check Python Documentation for more INFO)
l = bool(0) # The Number 0, any empty Data Types output False, None, and a __len__ func that returns 0 (Check Python Documentation for more INFO)

# In Built-Methods or Functions (Some Might Work with Other Data Types)
isinstance(j , bool)
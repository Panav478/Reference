"""
Data Types

Every variable has a data type classification which is decided how you assigned the variables values.
Don't bother to get confused, this is just an overview. The ones we need we will go in detail.
"""

# Built in Data Types
    # Text Type: str
    # Number Types: int , float , complex
    # Collection Types: range , tuple , dict , list , set , frozenset
    # Boolean Types : bool
    # Binary Types : bytes , bytearray , memoryview

# Setting Data Types vs Setting the Specific Data Type
a = "Hello World" # str
b = str("Hello World")	# str

c = 20	# int
d = int(20)	# int

e = 20.5 # float
f = float(20.5) # float

g = 1j # complex
h = complex(1j) # complex

i = range(6) # range
j = range(6) # range

k = (0 , 1 , 2) # tuple
l = tuple((0 , 1 , 2)) # tuple

m = {"Friends" : 57 , "Likes" : 189} # dict
n = dict(friends = 57 , likes = 189) # dict

o = {"Bob" , "Billy" , "Joe"} # set
p = set(("Bob" , "Billy" , "Joe")) # set

q = frozenset({"JoeMama" , "Johncena"}) # set
r = frozenset({"JoeMama" , "Johncena"}) # set

s = True
t = bool(3)

u = b"Hello"
v = bytes("Hello")

w = bytearray(5)
x = bytearray(5)

y = memoryview(bytes(5))
z = memoryview(bytes(5))
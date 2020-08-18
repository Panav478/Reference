"""
Python Numbers

These are the 3 different ways that bython represents numbers: integers, decimal number, and complex Numbers
"""

# Int --> Numbers that doesn't contain decimal values
a = 5
b = 3796488
c = -65749

type(a)
type(b)
type(c)

# Float --> Numbers that does contain decimal values
d = 1.1
e = 1.0
f = 1.86095

type(d)
type(e)
type(f)

# When using exponents you can use E or e to represent the power of 10
g = 12e4
h = 12E5
i = 24e3

type(g)
type(h)
type(i)

# Complex --> When you have an imaginary number (i or sqrt(-1)) shown with a j
j = 1j
k = 5 + 3j
l = -7j

type(j)
type(k)
type(l)

# Type Conversion --> Note: Can't convert a complex into another type
int1 = 5
float1 = 3.4
complex1 = 5j

intToFloat = float(int1)
intToComplex = complex(int1)
floatToInt = int(float1)
floatToComplex = complex(float1)

# Random Numbers
import random
random.randrange(1 , 11)
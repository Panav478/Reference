"""
Operators (Unlike the others .py files I copied these tables from websites so take some stuff as a grain of salt, might come in handy in the future though)

Types: 
       --> Arithmetic Operators
       --> Assignment Operators
       --> Comparison Operators
       --> Logical Operators
       --> Identity Operators
       --> Membership Operators
       --> Bitwise Operators

(Don't Sweat To Memorize This, You will probably learn it as you go.)
"""

"""
            Arithmetic Operators
Operators which are used to do basic mathematical operations (Note: If you want to perform more advanced mathematical tasks check out the Math Module)

Operator  |	      Name	    |  Example
    +	   |     Addition	    |   x + y	
    -	   |     Subtraction	    |   x - y	
    *	   |     Multiplication  |   x * y	
    /	   |     Division	    |   x / y	
    %	   |     Modulus	    |   x % y	  # Find What the Remainder Can Be (Ex: 5 % 3 = 2)
    **	   |     Exponentiation  |   x ** y	
    //	   |     Floor division  |   x // y  # Find How Much It can least be divided by useful when you have reminders (Ex: 5 // 3 = 1)
"""

"""
         Assignment Operators
Operators which are used to assign variables with a value

Operator  |	Example    |	 Same As	
   =	   |    x = 5	    |   x = 5	
   +=	   |    x += 3    |   x = x + 3	
   -=	   |    x -= 3    |	 x = x - 3	
   *=	   |    x *= 3    | 	 x = x * 3	
   /=	   |    x /= 3    |	 x = x / 3	
   %=	   |    x %= 3    |	 x = x % 3	# Find What the Remainder Can Be (Ex: 5 % 3 = 2)
   //=	   |    x //= 3   |	 x = x // 3	# Find How Much It can least be divided by useful when you have reminders (Ex: 5 // 3 = 1)
   **=	   |    x **= 3   |	 x = x ** 3	
   &=	   |    x &= 3    |	 x = x & 3	# Dunno, I have to figure this Assignment Operator out
   |=	   |    x |= 3    |	 x = x | 3	# Dunno, I have to figure this Assignment Operator out
   ^=	   |    x ^= 3    |	 x = x ^ 3	# Dunno, I have to figure this Assignment Operator out
   >>=	   |    x >>= 3   |	 x = x >> 3	# Dunno, I have to figure this Assignment Operator out
   <<=	   |    x <<= 3   |	 x = x << 3   # Dunno, I have to figure this Assignment Operator out
"""

"""
              Comparison Operators
Operators which are used to compare 2 values (All end to return a True or False value if printed, and is used commonly to create a condition for IF Statements)

Operator  |	      Name	           |  Example	
  ==	   |   Equal	                  |   x == y	
  !=	   |   Not equal	           |   x != y # Returns True when a number or a variable doesn't eqaul another (Ex: 5 != 3 , Console: True)
  >	   |   Greater than	           |   x > y	
  <	   |   Less than	           |   x < y	
  >=	   |   Greater than or equal to |   x >= y	
  <=	   |   Less than or equal to    |	 x <= y
"""

"""
                    Logical Operators
Operators which are used to Combine Conditional Statements

Operator  	                Description	                                          Example	
   and    |	 Returns True if both statements are true	                   |   x < 5 and  x < 10	
   or	   |    Returns True if one of the statements is true	            |   x < 5 or x < 4	
   not	   |    Reverse the result, returns False if the result is true     |	  not(x < 5 and x < 10)
"""

"""
                       Identity Operators
Operators that are used to compare if they are the same instance or not (Note: It does compare the value of the actual variable)              

Operator   |	                    Description	                     |    Example	
  is 	    |   Returns True if both variables are the same object	|   x is y 	
  is not   |	 Returns True if both variables are not the same object	|   x is not y
"""

"""
                                           Membership Operators
Operator that checks if some value is part of another (Ex: Checking a character is part of a string , Checking an item is part of a list)

Operator	                                 Description	                                    Example	
  in 	   |    Returns True if a sequence with the specified value is present in the object     |	x in y	
  not in  |	 Returns True if a sequence with the specified value is not present in the object | X not in y
"""

"""
                                          Bitwise Operators
Operators that are used to compare binary numbers. (Note: We wouldn't be working on this because we would be doing Machine Learning so ignore this for right now.)
Operator  |           Name	                                       Description
   & 	   |   AND	              |  Sets each bit to 1 if both bits are 1
   |	   |   OR	              |  Sets each bit to 1 if one of two bits is 1
   ^	   |   XOR	              |  Sets each bit to 1 if only one of two bits is 1
   ~ 	   |   NOT	              |  Inverts all the bits
   <<	   |   Zero fill left shift	|  Shift left by pushing zeros in from the right and let the leftmost bits fall off
   >>	   |   Signed right shift	|   Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

"""
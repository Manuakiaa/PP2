#Python Operators

#Operators are used to perform operations on variables and values.
#In the example below, we use the + operator to add together two values:
print(10 + 5)

#Python divides the operators in the following groups:
"""
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
"""
"""
Operator	Name	            Example 
+	       Addition	            x + y	
-	       Subtraction        	x - y	
*       	Multiplication      x * y	     
/       	Division	        x / y	
%	       Modulus	            x % y	
**      	Exponentiation	    x ** y	
//	       Floor division	    x // y
"""

"""
==	Equal	                        x == y	
!=	Not equal	                    x != y	
>	Greater than	                x > y	
<	Less than	                    x < y	
>=	Greater than or equal to	    x >= y	
<=	Less than or equal to        	x <= y
"""

"""and        	Returns True if both statements are true	                     x < 5 and  x < 10	
or	            Returns True if one of the statements is true                    x < 5 or x < 4	
not	            Reverse the result, returns False if the result is true	not      (x < 5 and x < 10)"""

"""is 	Returns True if both variables are the same object	        x is y	
is not	Returns True if both variables are not the same object      	x is not y"""

"""in 	Returns True if a sequence with the specified value is present in the object    	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y"""

#Operator precedence describes the order in which operations are performed.
#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3))

#Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:
print(100 + 5 * 3)

#The precedence order is described in the table below, starting with the highest precedence at the top:
"""()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR"""

#Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:
print(5 + 4 - 7 + 3)
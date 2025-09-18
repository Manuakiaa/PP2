#There are three numeric types in Python:
int
float
complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
#Integers:
x = 1
y = 35656222554887711
z = -3255522

#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
#Floats:
x = 1.10
y = 1.0
z = -35.59

#Float can also be scientific numbers with an "e" to indicate the power of 10.
#Floats:
x = 35e3
y = 12E4
z = -87.7e100

#Complex numbers are written with a "j" as the imaginary part:
#Complex:
x = 3+5j
y = 5j
z = -5j

#Convert from one type to another:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)

#Random Number
import random

print(random.randrange(1, 10))
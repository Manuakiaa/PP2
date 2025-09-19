#Python Variables
#In Python, variables are created when you assign a value to it:

#Example
#Variables in Python:
x = 5
y = "Hello, World!"

#Creating Variables
x = 4       # x is of type int
y = "Sally" # y is now of type str
print(x)
print(y)

#If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#You can get the data type of a variable with the type() function.  
x = 5
y = "John"
print(type(x))
print(type(y))

#This will create two variables:

a = 4
A = "Sally"
#A will not overwrite a

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

# my_variable_name or MyVariableName or myVariableName #multi words

#Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"

#One Value to Multiple Variables
x = y = z = "Orange"

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  #apple
print(y)  #banana
print(z)  #cherry

#The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)  #Python is awesome

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)  #Python is awesome

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)   #Python is awesome

#For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)  #Good

x = 5
y = "John"
print(x + y) #Error

#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)


#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.
    
#Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()  #Python is awesome

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()   #Python is fantastic

print("Python is " + x)  #Python is awesome
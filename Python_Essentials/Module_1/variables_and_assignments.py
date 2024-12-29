# Variables and assignment 

"""
Python is not a very strongly typed languuage.
You do not have to worry about the type of the data stored in the variable.
"""
# variable 1 
height = 1000 # variable is assigned a value int 
height = "1000" # same variable can be assigned to a string 
# No type checking is done in python

# creating new variables from existing ones 
first_name = "John"
last_name = "Doe"
full_name = f"{first_name} {last_name}" # creation of new variable from existing ones 

name = "John"
new_name = name 
name = "Alfedro"
print(new_name)
print(name) # Python did not auto update both the variables.
# one variable state did not change.


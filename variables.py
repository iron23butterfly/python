# Declare a variable and initialize it
f = 0
print (f)

# re-declaring the variable works
f = "abc"
print (f)

# ERROR: variables of different types cannot be combined
#print ("string type " + 123)
print ("string type " + str(123))

# Global vs. local variables in functions
def someFunction():
  #global f - over writes any other f
  f = "def"
  print ("someFunction(): ", f)

someFunction()
print (f) 

del f
#print (f)
#This will give an error

# OUTPUT

#0
#abc
#string type 123
#someFunction():  def
#abc

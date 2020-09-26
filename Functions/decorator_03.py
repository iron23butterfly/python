# decorator_02.py is written like this with decorator symbol @

def f1(f): 
def f2(): 
print ("f2 before function call") 
f() 
print ("f2 after function call") 
return f2 # will return address of function f2 
 
@f1 # address of f3 will be sent as arg to function f1 
def f3(): 
print ("this is f3") 
 
f3() # This is essentially a wrapper to @f1-and-f3 

# OUTPUT 
# f2 before function call 
# this is f3 
# f2 after function call

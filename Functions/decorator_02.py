def f1(f): 
def f2(): 
print ("f2 before function call") 
f() 
print ("f2 after function call") 
return f2 # will return address of function f2 
 
def f3(): 
print ("this is f3") 
 
x = f1(f3) # Function f1 has the address of f3 in the arg 
           # but x stores the address of function f2 
x() # function call for f2 
 
# OUTPUT 
# f2 before function call 
# this is f3 
# f2 after function call 

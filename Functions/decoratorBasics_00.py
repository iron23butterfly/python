def f1():
    def f2():
        print ("this is f2")
    return f2 #will return address of function f2

x = f1() # will have address of f2
print (type(x))
x() # function call for f2

# OUTPUT
# <class 'function'>
# this is f2

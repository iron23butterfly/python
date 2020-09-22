# define a basic function
def func1():
  print ("I am a function")

# function that takes arguments
def func2(arg1, arg2):
  print (arg1, " ", arg2)

# function that returns a value
def cube(x):
  return x*x*x

# function with default value for an argument
def power(num, x=1):
  result = 1;
  for i in range(x):
    result = result * num  
  return result

#function with variable number of arguments
def multi_add(*args):
  result = 0;
  for x in args:
    result = result + x
  return result

func1()
print("\n")
print (func1())
print("\n")
print ("func1: ", func1)
func2(10,20)
print("\n")
print (func2(10,20))
print("\n")
print ("cube(3): ", cube(3))
print ("power(2): ",power(2))
print ("power(2,3): ", power(2,3))
print ("power(x=3, num=2): ", power(x=3, num=2))
print ("multi_add(4,5,10,4): ", multi_add(4,5,10,4))

#OUTPUT:

#I am a function

#I am a function
#None

#func1: <function func1 at 0x030EC340>
#10   20

#10   20
#None

#cube(3):  27
#power(2):  2
#power(2,3):  8
#power(x=3, num=2):  8
#multi_add(4,5,10,4):  23


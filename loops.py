# Example file for working with loops
#

def main():
  x = 0
  
  # define a while loop
  while (x < 5):
     print (x)
     x = x + 1

  # define a for loop
  for x in range(5,10):
    print (x)
    
  # use a for loop over a collection
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for d in days:
    print (d)
  
  # use the break and continue statements
  for x in range(5,10):
    #if (x == 7): break
    #if (x % 2 == 0): continue
    print (x)
  
  #using the enumerate() function to get index 
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for i, d in enumerate(days):
    print (i, d)
  
if __name__ == "__main__":
  main()

#OUTPUT
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9
#Mon
#Tue
#Wed
#Thu
#Fri
#Sat
#Sun
#5
#6
#7
#8
#9
#0 Mon
#1 Tue
#2 Wed
#3 Thu
#4 Fri
#5 Sat
#6 Sun

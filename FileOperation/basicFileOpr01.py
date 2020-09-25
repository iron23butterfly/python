# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  f = open("textfile.txt","w+")
  
  # Open the file for appending text to the end
  # f = open("textfile.txt","a+")

  # write some lines of data to the file
  for i in range(10):
    f.write("This is line %d\r" % (i+1))
  
  # close the file when done
  f.close()
  
  # Open the file back up and read the contents
  f = open("textfile.txt","r")
  if f.mode == 'r': # check to make sure that the file was opened
    # use the read() function to read the entire file
    # contents = f.read()
    # print (contents)
    
    fl = f.readlines() # readlines reads the individual lines into a list
    for x in fl:
      print (x)
    
if __name__ == "__main__":
  main()
  
  # OUTPUT
  # This is line  1
  # 
  # This is line  2
  # 
  # This is line  3
  # 
  # This is line  4
  # 
  # This is line  5
  # 
  # This is line  6
  # 
  # This is line  7
  # 
  # This is line  8
  # 
  # This is line  9
  # 
  # This is line  10

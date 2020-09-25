# Example file for working with os.path module
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
  # Print the name of the OS
  print (os.name)
  
  # Check for item existence and type
  print ("Item exists: " + str(path.exists("textfile.txt")))
  print ("Item is a file: " + str(path.isfile("textfile.txt")))
  print ("Item is a directory: " + str(path.isdir("textfile.txt")))
  
  # Work with file paths
  print ("Item's path: " + str(path.realpath("textfile.txt")))
  print ("Item's path and name: " + str(path.split(path.realpath("textfile.txt"))))
  
  # Get the modification time
  t = time.ctime(path.getmtime("textfile.txt"))
  print (t)
  print (datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
  
  # Calculate how long ago the item was modified
  td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
  print ("It has been " + str(td) + " since the file was modified")
  print ("Or, " + str(td.total_seconds()) + " seconds")

if __name__ == "__main__":
  main()

#   OUTPUT
#
# nt
# Item exists: True
# Item is a file: True
# Item is a directory: False
# Item's path: C:\Users\fsandhyx\PycharmProjects\Ex_Files_Learning_Python\Exercise Files\Ch4\textfile.txt
# Item's path and name: ('C:\\Users\\fsandhyx\\PycharmProjects\\Ex_Files_Learning_Python\\Exercise Files\\Ch4', 'textfile.txt')
# Thu Sep 24 17:29:56 2020
# 2020-09-24 17:29:56.094455
# It has been 0:09:40.891172 since the file was modified
# Or, 580.891172 seconds

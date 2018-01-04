import sys
from random import *
from math import *
from rando import *

# check to see if user entered enough arguments
if len(sys.argv) < 2: # argv is a list of arguments; item 0 is the filename rando.py
    print 'Usage: python random.py <# of random numbers> <min number generated> <max number generated>'
    exit(-1) # nonzero return value indicates things didn't go right

if __name__ == "__main__":
  howmany = int(sys.argv[1])
  minr = int(sys.argv[2])
  maxr = int(sys.argv[3])
  randomlist = []
  while len(randomlist) < howmany:
    randomlist.append(randrange(minr, maxr))
  print ("You asked for %i random numbers between %i and %i." %(howmany,minr,maxr))
  print(randomlist)
#  print ("Mean is %f" %(mean(randomlist)))
#  print ("Median is %f" %(median(randomlist)))
#  print ("Mode is ", oldmode(randomlist))
#  print ("Mode2 is ", mode(randomlist))

# Open a file, put the random numbers into it, and close it.
f = open('random_numbers', 'w+')
i = 1
for num in randomlist:
  s = str(num)
  f.write(str(i) + ": " + s + "\n")
  i += 1
f.close

# Now open the file and read all the stuff.
print("Random numbers read from file:")
f = open('random_numbers', 'r')
lines = f.readlines()
for i in lines:
  print i



# Open main.tex file, read-only, read it into temp buffer, close it
# filename = sys.argv[1]
# f = open(filename, 'r')
# temp = f.read()
# f.close()

# Open metadata file, read in lines to buffer, print lines
# f = open('.. Orig/metadata', 'r') # Need to get path, etc.
# lines = f.readlines()
# for i in xrange(lines):
#   print lines[i]

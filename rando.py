#!/usr/bin/env python

# Want user to be able to type random.py and three command-line arguments: how many random numbers to generate,
# and a min number generated and a max number generated. The program generates the numbers, then prints them
# out on separate lines.

# sys.argv is a list in Python, which contains the command-line arguments passed to the script
# If you are gonna work with command line arguments, you probably want to use sys.argv.
# To use sys.argv, you will first have to import the sys module.
import sys

# import stuff needed for random number generation
from random import *
from math import *

# check to see if user entered enough arguments
if len(sys.argv) < 2: # argv is a list of arguments; item 0 is the filename rando.py
    print 'Usage: python random.py <# of random numbers> <min number generated> <max number generated>'
    exit(-1) # nonzero return value indicates things didn't go right


def mean(data):
  """mean(data) -> arithmetic mean of data, which is a sequence of numbers."""
  total = 0
  for y in range(len(data)):
    total += data[y]
  m = (total * 1.0) / len(data)
  return m

def median(data):
  """median(data) -> median of data, which is a sequence of numbers."""
  l = sorted(data)
  if len(l) % 2 == 1: # we have an odd number of random numbers
    medposition = int(floor((len(l) / 2))) # can remove floor?
    med = (l[medposition])
  else: # we have an even number of random numbers
    medposition1 = (len(l) / 2) - 1 
    medposition2 = len(l) / 2
    med = ((l[medposition1] + l[medposition2]) * 1.0) / 2 # can use mean() here
  return med


def oldmode(data):
  a = sorted(data)
  countlist = [] # create list of counts of each number in random list
  for position in range (len(a)):
    countlist.append(a.count(a[position]))
  b = sorted(countlist)
  highcount = b[(len(a) - 1)] # last number in the list is the highest count
  modelist = [] # create list of numbers with counts that match the highest count
  for position in range(len(a)):
    if a.count(a[position]) == highcount:
      modelist.append(a[position])
  deduped_modeset = set(modelist) # remove the duplicate numbers by converting the list to a set
  return deduped_modeset

def mode(data):
  # Store the count of each number in data in a dictionary ("histogram").
  counts = {}  
  for number in data:
    # If number is not yet in counts, create an entry, counts[number], 
    # and set it to 1.
    if number not in counts:
      counts[number] = 1
    # Otherwise, increment counts[number] to articulate that you've found 
    # another instance of number.
    else: # counts[number] already exists!
      counts[number] += 1

  # Now find the key(s) in counts with the max value(s).

  # Find the maximum count in the dictionary.
  max_count = -1
  #for (key, value) in counts.items():
  #for key in counts.keys():
  for value in counts.values():
    max_count = max(max_count, value)

  # Now find the keys whose values are max_count.
  modelist = set()
  for (key, value) in counts.items():
    if value == max_count: # <-- this is a winner!
      modelist.add(key)

  return modelist


if __name__ == "__main__":
  howmany = int(sys.argv[1])
  minr = int(sys.argv[2])
  maxr = int(sys.argv[3])
  randomlist = []
  while len(randomlist) < howmany:
    randomlist.append(randrange(minr, maxr))
  print ("You asked for %i random numbers between %i and %i." %(howmany,minr,maxr))
  print(randomlist)
  print ("Mean is %f" %(mean(randomlist)))
  print ("Median is %f" %(median(randomlist)))
  print ("Mode is ", oldmode(randomlist))
  print ("Mode2 is ", mode(randomlist))













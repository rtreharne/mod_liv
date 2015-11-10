#!/usr/bin/env python

# Example script for CDTcommando
# Campaign: Python
# Mission: Lock and Load
# R. Treharne
# Feb 10 2015

#plot of 2D data from two column .csv file

from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import csv
import re
import sys

filename = sys.argv[1]
#linestyle = sys.argv[2]

#filename = 'data.csv'
linestyle = 'o-'

# Check to see if first row in .csv file contains alpha characters
afile = open(filename, 'r+')
csvreader = csv.reader(afile)
row = csvreader.next()
lst = list(row[0])
header =  re.sub('  +', ',', row[0])
header = header.split(',')
skip = 0

#If first row of data contains alpha characters then set skip
for i in range (0,len(lst)):
      if lst[i].isalpha() == True:
              skip = 1

# Load data to arrays
x = loadtxt(filename, unpack = True, usecols = [0], skiprows = skip)
y = loadtxt(filename, unpack = True, usecols = [1], skiprows = skip) 

plot(x,y, linestyle, color='red')
xlabel(header[0])
#ylabel(header[1])

show()

#Copyrights SUDARSHAN
#The University of Texas at Dallas

import sys
import math , os

def read_file(): #Read the file
    if len(sys.argv) < 3:
        print "Enter a valid Training Set file name: ", 
        filename = sys.stdin.readline().strip()
    else:
        filename = sys.argv[1]

    try:
        fname = open(filename, "r")
    except IOError:
        print "Error: The file '%s' was not found on this system." % filename
        sys.exit(0)

    return fname

def read_file_2(): #Read the file
    if len(sys.argv) < 4:
        print "Enter a valid Training Set file name: ", 
        filename = sys.stdin.readline().strip()
    else:
        filename = sys.argv[2]

    try:
        fname = open(filename, "r")
    except IOError:
        print "Error: The file '%s' was not found on this system." % filename
        sys.exit(0)

    return fname
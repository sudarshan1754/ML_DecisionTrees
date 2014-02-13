#Copyrights SUDARSHAN
#The University of Texas at Dallas

import sys
import math , os

def traverseTree(row, tree):
    """Fucntion to traverse the tree and find the class to 
    which the instance belogs to"""
    for key, val in tree.iteritems():
        while(key != '0' or key != '1'):
            if key in row:
                if row[key] in val:

                    if type(val[row[key]]) == str:

                        return val[row[key]]

                    for k, v in val[row[key]].iteritems():

                        key = k
                        val = v

        break
    

def Comparedata(fread, tree): #To read the data in the file
    lines = [line.strip() for line in fread.readlines()]

    lines.reverse()

    att = [attr.strip() for attr in lines.pop().split(",")] 
    
    Class_attr = att[-1]   #To get the class attribute
    
    lines.reverse()  #To go back to first line

    data_list = []   #To create a list as Shown below
    for line in lines:
        data_list.append(dict(zip(att,
            [datum.strip() for datum in line.split(",")])))

    Hits = 0
    Miss = 0
    for i, row in enumerate(data_list):

        dtClass = traverseTree(row, tree)
        if dtClass == row[Class_attr]:
        	Hits = Hits + 1
        else:

        	Miss = Miss + 1

    #To calculate Accuracy
    Acc = Hits/float(i+1)
    print "Classified:" + str(Hits) + "\n" + "Misclassified:" + str(Miss) + "\n" +  "Total Instances:" + str(i + 1)
    return Acc
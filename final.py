#Copyrights SUDARSHAN
#The University of Texas at Dallas

import sys
import math , os
from Accuracy import *
from printTree import *
from readFile import *
#from pruning import *
from Info import *
#from var import *

   
def Select_attribute(data, attributes, target_attr, infogain):
    data = data[:]
    best_gain = 0.0
    best_attr = None

    
    for attr in attributes:
        gain = infogain(data, attr, target_attr)
        if (gain >= best_gain and attr != target_attr):
            best_gain = gain
            best_attr = attr

    return best_attr

def exampleSet(data, attr, value):

    data = data[:]
    rtn_lst = []
    
    if not data:
        return rtn_lst
    else:
        record = data.pop()
        if record[attr] == value:
            rtn_lst.append(record)
            rtn_lst.extend(exampleSet(data, attr, value))

            return rtn_lst
        else:
            rtn_lst.extend(exampleSet(data, attr, value))

            return rtn_lst


def classification(record, tree):

    if type(tree) == type("string"):
        return tree

    else:
        attr = tree.keys()[0]
        t = tree[attr][record[attr]]

        return classification(record, t)

def classify(tree, data):

    data = data[:]
    classifi = []
    
    for record in data:
        classifi.append(classification(record, tree))

    return classifi

def createTree(data, attributes, target_attr, fitness_func):

    data = data[:]
    vals = [record[target_attr] for record in data]
    
    default = majority_value(data, target_attr)

    if not data or (len(attributes) - 1) <= 0:
        return default

    elif vals.count(vals[0]) == len(vals):
        return vals[0]
    
    else:

        best = Select_attribute(data, attributes, target_attr,
                                fitness_func)

        tree = {best:{}}

        for val in get_values(data, best):
            subtree = createTree(
                exampleSet(data, best, val),
                [attr for attr in attributes if attr != best],
                target_attr,
                fitness_func)

            tree[best][val] = subtree

    return tree


def read_data(fread): #To read the data in the file
    lines = [line.strip() for line in fread.readlines()]
    
    lines.reverse()

    att = [attr.strip() for attr in lines.pop().split(",")] 
    
    Class_attr = att[-1]   #To get the class attribute
    
    lines.reverse()  #To go back to first line

    data_list = []   #To create a list as Shown below
    for line in lines:
        data_list.append(dict(zip(att,
            [datum.strip() for datum in line.split(",")])))

    examples = data_list[:]

    tree = createTree(data_list, att, Class_attr, gain)

    classification = classify(tree, examples)

    return tree


if __name__ == "__main__":
    fname = read_file()
    
    tre = read_data(fname)

    fname.close()

    fname_2 = read_file_2()

    Accuracy = Comparedata(fname_2, tre)
    print "Accuracy:" + str(Accuracy * 100) + "%"
    
    

    ToPrint = sys.argv[3]
    if ToPrint == 'yes':
        print_tree(tre, "")
    else:
        fname.close()
    

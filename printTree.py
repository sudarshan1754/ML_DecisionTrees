#Copyrights SUDARSHAN
#The University of Texas at Dallas

def print_tree(tree, str):
    if type(tree) == dict:
        print "%s%s:" %(str, tree.keys()[0])
        for item in tree.values()[0].keys():

            print "%s%s" % (str, item)
            print_tree(tree.values()[0][item], str + "   |")
    else:
        print "%s:%s" % (str, tree)



def majority_value(data, target_attr):

    data = data[:]
    return most_frequent([record[target_attr] for record in data])
    
def most_frequent(lst):

    lst = lst[:]
    highest_freq = 0
    most_freq = None

    for val in unique(lst):
        if lst.count(val) > highest_freq:
            most_freq = val
            highest_freq = lst.count(val)
    return most_freq

def unique(lst):

    lst = lst[:]
    unique_lst = []

    for item in lst:
        if unique_lst.count(item) <= 0:
            unique_lst.append(item)
    return unique_lst

def get_values(data, attr):
    
   
    data = data[:]
    return unique([record[attr] for record in data])


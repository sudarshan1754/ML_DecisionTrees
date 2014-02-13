#Copyrights SUDARSHAN
#The University of Texas at Dallas

import math

def entropy(data, Class_attr):

    val_freq = {}
    data_entropy = 0.0
 
    for record in data:
        if (val_freq.has_key(record[Class_attr])):
            val_freq[record[Class_attr]] += 1.0
        else:
            val_freq[record[Class_attr]] = 1.0

    for freq in val_freq.values():

        data_entropy += (-freq/len(data)) * math.log(freq/len(data), 2) 
 
    return data_entropy

    
def gain(data, attr, Class_attr):

    val_freq = {}
    subset_entropy = 0.0

    for record in data:
        if (val_freq.has_key(record[attr])):
            val_freq[record[attr]] += 1.0

        else:
            val_freq[record[attr]] = 1.0

    for val in val_freq.keys():

    	val_prob = val_freq[val] / sum(val_freq.values())
        data_subset = [record for record in data if record[attr] == val]

        subset_entropy += val_prob * entropy(data_subset, Class_attr)
    return (entropy(data, Class_attr) - subset_entropy)
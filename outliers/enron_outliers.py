#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
# print "data_dict: ",data_dict
features = ["salary", "bonus"]
data_dict.pop( "TOTAL", 0 )
data = featureFormat(data_dict, features)


### your code below
max_bonus = 0

for point in data:
    salary = point[0]
    bonus = point[1]
    # print "salary : ",salary, "bonus : ",bonus
    
    if max_bonus < bonus:
     max_bonus = bonus
    matplotlib.pyplot.scatter( salary, bonus )
    

all_data = []

for key in data_dict:
    name = key
    salary = data_dict[key]['salary']
    bonus = data_dict[key]['bonus']
    
    if salary == 'NaN':
        salary = 0
    if bonus == 'NaN':
        bonus = 0
    
    all_data.append((name, salary, bonus))
    print "Name : ", name, "salary : ",salary, "bonus : ",bonus

all_data = sorted(all_data, key = lambda t:t[2], reverse=True )
outliers = all_data[0:5]

print "max_bonus : ", max_bonus

print outliers
matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()




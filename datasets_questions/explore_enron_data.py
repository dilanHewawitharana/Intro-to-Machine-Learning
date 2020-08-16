#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print(len(enron_data))
print(len(enron_data["SKILLING JEFFREY K"]))

print(enron_data["SKILLING JEFFREY K"])

poi_sum = sum(v.get("poi", 0) == 1 for v in enron_data.values())
print(poi_sum)

# poi_names = pickle.load(open("../final_project/poi_names.txt", "r"))
# print(len(poi_names))

print("PRENTICE JAMES.total_stock_value")

print "PRENTICE JAMES.total_stock_value :" , enron_data["PRENTICE JAMES"]["total_stock_value"] 

print "COLWELL WESLEY.from_this_person_to_poi :" , enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "JEFFREY SKILLING K.exercised_stock_options :" , enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "JEFFREY SKILLING K.total_payments :" , enron_data["SKILLING JEFFREY K"]["total_payments"]
print "KENNETH LAY.total_payments :" , enron_data["LAY KENNETH L"]["total_payments"]
print "ANDREW FASTOW.total_payments :" , enron_data["FASTOW ANDREW S"]["total_payments"]

no_of_salary = sum(v.get("salary", 0) != "NaN" for v in enron_data.values())
print "No_of_salary :", no_of_salary

no_of_email_address = sum(v.get("email_address", 0) != "NaN" for v in enron_data.values())
print "No_of_email_address :", no_of_email_address

x = sum(v.get("total_payments", 0) == "NaN" for v in enron_data.values())
y = len(enron_data)

print "Percentage of people 'NaN' for their total payments :", (float(x)/y) * 100 , "%"

z = sum(((v.get("poi", 0) == 1) and (v.get("total_payments", 0) == "NaN")) for v in enron_data.values())
print z
print(poi_sum)
print(x)


 





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
import sys
import pickle
sys.path.append("../tools/")

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

poi_count_dataset = 0
for employee in enron_data.keys():
    poi_count_dataset += enron_data.get(employee).get("poi")
print "There are %d POIs" % poi_count_dataset

poi_list = open("../final_project/poi_names.txt", "r")

poi_count_file = 0
for line in poi_list:
    if line.startswith("(y)") or line.startswith("(n)"):
        poi_count_file += 1

print"There are %d POIs in the file" % poi_count_file

# poi_0 = enron_data.keys()[0]
# for feature in enron_data[poi_0]:
#     print feature


count_quant_salary = 0
count_email_known = 0

poi_list = []
count_poi_missing_payment = 0

for person in enron_data.keys():
    if  "@" in enron_data[person]["email_address"]:
        count_email_known += 1

    if isinstance(enron_data[person]["salary"], (int, long)):
        count_quant_salary += 1

    if enron_data[person]["poi"]:
        poi_list.append(enron_data[person])
        if enron_data[person]["total_payments"] == 'NaN':
            count_poi_missing_payment += 1

print "Salary quantitative for %d employees, email known for %d" % (count_quant_salary, count_email_known)

print "Missing payments: %d, total percentage: %f" % (count_poi_missing_payment, float(count_poi_missing_payment)/len(poi_list))


persons_missing_total = 10
for person in enron_data.keys():
    if enron_data[person]['total_payments'] == 'NaN':
        persons_missing_total += 1

print "New percentage of NaN: %f" % (float(persons_missing_total)/(len(enron_data.keys()) + 10))



#!/usr/bin/python3

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

# import joblib


# enron_data = joblib.load(open("../final_project/final_project_dataset_modified.pkl", "rb"))
import pickle
enron_data = pickle.load(open("C:/Users/ASUS/Downloads/udacity-Intro-to-Machine-Learning-master/udacity-Intro-to-Machine-Learning-master/final_project/final_project_dataset.pkl",'rb'))
print(len(enron_data.values()))
var1=enron_data.values()
cnt=0
cnt1=0
for i in enron_data:
    for j in i:
        cnt+=1
        if(enron_data[i]['poi'] == 1):
            cnt1+=1
print(cnt)
print(cnt1)
cntsal=0
cnteml=0
print(enron_data['PRENTICE JAMES'])
print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])
print(enron_data['LAY KENNETH L'])
for i in enron_data:
    if(enron_data[i]["salary"]!="NaN"):
        cntsal+=1
    if(enron_data[i]["email_address"]!="NaN"):
        cnteml+=1
print(cntsal)
print(cnteml)
people=0 ;cntnan=0
for i in enron_data:
    people+=1
    if(enron_data[i]["poi"]==1):
        if(enron_data[i]["total_payments"]=="NaN"):
            cntnan+=1
print((cntnan*100)/people)
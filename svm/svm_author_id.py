#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
from enum import auto
from math import gamma
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
#features_train = features_train[:int(len(features_train)/100)]
#labels_train = labels_train[:int(len(labels_train)/100)]


#########################################################
### your code goes here ###
from sklearn.svm import SVC
clf=SVC(kernel='rbf',C=10000)
t0=time()
clf.fit(features_train,labels_train)
print("training time",round(time()-t0,3),"s")
t1=time()
#pred=clf.predict(features_test)
#print(pred[10])
#print(pred[26])
#print(pred[50])
print(sum(clf.predict(features_test)==1))
print("prediction time",round(time()-t1,3),"s")
from sklearn.metrics import accuracy_score
#print(accuracy_score(pred,labels_test))


#########################################################

#########################################################
'''
You'll be Provided similar code in the Quiz
But the Code provided in Quiz has an Indexing issue
The Code Below solves that issue, So use this one
'''

#features_train = features_train[:int(len(features_train)/100)]
#labels_train = labels_train[:int(len(labels_train)/100)]

#########################################################

#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

t0 = time() #start time

from sklearn.svm import SVC
#clf = SVC(kernel="linear")
clf = SVC(kernel="rbf",C=10000)

clf.fit(features_train, labels_train)

print "training time:", round(time()-t0, 3), "s"

t1 = time() #predict time

pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)

print "predict time:", round(time()-t1, 3), "s"

print accuracy

print "Predict for 10,26,50 : ", clf.predict([features_test[10],features_test[26],features_test[50]])

print "Length : ", len(features_test)

print sum(pred)

#print "Predict for 10,26,50 : ", clf.predict([features_test[1:10]])
#########################################################



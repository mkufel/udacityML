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

from sklearn import svm
from sklearn.metrics import accuracy_score
import numpy as np

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf = svm.SVC(kernel='rbf', C=10000.0)
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "training time:", round(time()-t1, 3), "s"

print accuracy_score(pred, labels_test)

print "Accuracy 10th elt: " + str(pred[10])
print "Accuracy 26th elt: " + str(pred[26])
print "Accuracy 50th elt: " + str(pred[50])

unique, counts = np.unique(pred, return_counts=True)
print dict(zip(unique, counts))

print "Number of test samples classified as 1: " + str(sum(pred == 1))

#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from r import readxml
import os
from sklearn import svm


NOF = 1893 # the number of features
numofsen = []  # the number of sentences
numofsen.append(0)
vecfeature = []
for filename in os.listdir(r'newtraindata/'):
    print 'in svm.py ' + filename
    vecfeature += readxml('newtraindata/' + filename, numofsen)  # append all traindata together

data = []
target = []
for line in vecfeature:
    data.append(line[:-1])
    target.append(line[NOF])
print target
clf = svm.SVC(kernel='rbf', C=0.5, gamma=1)
clf.fit(data, target)


def getopn(wlist):
    return clf.predict(wlist)

# vim: sw=4 ts=4 sts=4 expandtab

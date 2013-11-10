#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from r import readxml
import os
from sklearn.naive_bayes import BernoulliNB


NOF = 7  # the number of features
numofsen = []  # the number of sentences
numofsen.append(0)
vecfeature = []
for filename in os.listdir(r'traindata/'):
    print 'in berbayes.py ' + filename
    vecfeature += readxml('traindata/' + filename, numofsen)  # append all traindata together
data = []
target = []
for line in vecfeature:
    data.append(line[:-1])
    target.append(line[NOF])
gnb = BernoulliNB()
gnb.fit(data, target)


def getopn(wlist):
    return gnb.predict(wlist)




# vim: sw=4 ts=4 sts=4 expandtab

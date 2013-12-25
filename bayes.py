#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from r import readxml
import os


NOF = 34  # the number of features
numofsen = []  # the number of sentences
numofsen.append(0)
vecfeature = []
for filename in os.listdir(r'traindata/'):
    print 'in bayes.py ' + filename
    vecfeature += readxml('traindata/' + filename, numofsen)  # append all traindata together
countop = 0.0
for line in vecfeature:
    if line[NOF] == 1:
        countop += 1   # count the number of opnionated words
py = countop / numofsen[0]


"""
compare two vectors
"""
def same(src, dest):
    for i in range(0, NOF):
        if src[i] != dest[i]:
            return 0
    return 1

"""
get the result of bayes
"""


def getopn(wlist):
    x = 0.0
    xandop = 0.0
    for line in vecfeature:
        if same(wlist, line):
            x += 1
            if line[NOF] == 1:
                xandop += 1
    pxgiveny = xandop / countop
    px = x / numofsen[0]
    if px == 0.0:
        return -1
    pygivenx = py * pxgiveny / px
    if pygivenx > 0.5:   # ?
        return 1
    else:
        return 0


# vim: sw=4 ts=4 sts=4 expandtab

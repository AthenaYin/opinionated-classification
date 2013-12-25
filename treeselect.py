#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import os
from r import readxml
import cmath

NOF = 1665
numofsen = []  # the number of sentences
numofsen.append(0)
vecfeature = []
y = []
C = 0.0
notC = 0.0
Ct = []
IGt = []
t = []
for i in range(0, NOF):
    Ct.append(0.0)
    IGt.append(0.0)
    t.append(0.0)
temp = []
for filename in os.listdir(r'ans/'):
    temp = readxml('ans/' + filename, numofsen)
    for line in temp:
        if line[NOF] == 1:
            C += 1
            for i in range(0, NOF):
                if line[i]:
                    Ct[i] += 1
        else:
            notC += 1
        for i in range(0, NOF):
            if line[i]:
                t[i] += 1
PC = C / (C + notC)
PnotC = 1-PC
HC = - (PC * cmath.log(PC, 2)) - (PnotC * cmath.log(PnotC, 2))
print C, notC
print t
print Ct
for i in range(0, NOF):
    Pt = (t[i] + 1) / (C + notC + 1)
    Pnott = 1 - Pt
    PCt = (Ct[i] + 1) / (t[i] +1)
    PnotCt = 1 - PCt
    PCnott = (C - Ct[i] + 1) / (C + notC - Ct[i] + 1)
    PnotCnott = 1 - PCnott
    IGt[i] += HC
    IGt[i] += ((PCt * cmath.log(PCt, 2)) + (PnotCt * cmath.log(PnotCt, 2))) * Pt
    IGt[i] += ((PCnott * cmath.log(PCnott, 2)) + (PnotCnott * cmath.log(PnotCnott, 2))) * Pnott
mlist = []
print t
for i in range(0, NOF):
    if t[i] > 10.0:
        print t[i]
        print i

print mlist
#print IGt
# vim: sw=4 ts=4 sts=4 expandtab

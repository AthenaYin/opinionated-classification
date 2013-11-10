#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import os
from r import readxml
import cmath

NOF = 7
numofsen = []  # the number of sentences
numofsen.append(0)
vecfeature = []
y = []
C = 0.0
notC = 0.0
Ct = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
IGt = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
t = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
for filename in os.listdir(r'traindata/'):
    temp = readxml('traindata/' + filename, numofsen)
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
    Pt = t[i] / (C + notC)
    Pnott = 1 - Pt
    PCt = Ct[i] / t[i]
    PnotCt = 1 - PCt
    PCnott = (C - Ct[i]) / (C + notC - Ct[i])
    PnotCnott = 1 - PCnott
    IGt[i] += HC
    IGt[i] += ((PCt * cmath.log(PCt, 2)) + (PnotCt * cmath.log(PnotCt, 2))) * Pt
    IGt[i] += ((PCnott * cmath.log(PCnott, 2)) + (PnotCnott * cmath.log(PnotCnott, 2))) * Pnott
print IGt
# vim: sw=4 ts=4 sts=4 expandtab

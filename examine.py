#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
import xml.etree.ElementTree as ET
import os

reload(sys)
sys.setdefaultencoding('utf-8')

A = 0.0
B = 0.0
C = 0.0
D = 0.0

f1 = open('FN.txt', 'w')
f2 = open('FP.txt', 'w')

for filename in os.listdir('svmans/'):
    tree1 = ET.parse('svmans/' + filename)
    tree2 = ET.parse('ans/' + filename)
    root1 = tree1.getroot()
    root2 = tree2.getroot()
    for child1 in root1:
        for child2 in root2:
            if child2.attrib['id'] == child1.attrib['id']:
                for childd1 in child1:
                    for childd2 in child2:
                        if childd1.tag == 'sentence' and childd2.attrib['id'] == childd1.attrib['id']:
                            if childd1.attrib['opinionated'] == 'Y':
                                if childd2.attrib['opinionated'] == 'Y':
                                    A += 1
                                else:
                                    C += 1
                                    f2.write(childd1.text + '\n')
                            else:
                                if childd2.attrib['opinionated'] == 'Y':
                                    B += 1
                                    f1.write(childd1.text + '\n')
                                else:
                                    D += 1
                            break
                break
print A, B, C, D
print 'precision:'
print A / (A + C)
print 'recall'
print A / (A + B)

# vim: sw=4 ts=4 sts=4 expandtab

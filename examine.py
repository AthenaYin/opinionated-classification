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
cc = 0

for filename in os.listdir('count1ans/'):
    tree1 = ET.parse('count1ans/' + filename)
    tree2 = ET.parse('newtestdata/' + filename)
    root1 = tree1.getroot()
    root2 = tree2.getroot()
    for child1 in root1:
        for child2 in root2:
            if child2.attrib['id'] == child1.attrib['id']:
                for childd1 in child1:
                    for childd2 in child2:
                        if not childd2.attrib.has_key('polarity'):
                            continue
                        if childd1.tag == 'sentence' and childd2.attrib['id'] == childd1.attrib['id']:
                            cc += 1
                            if cc % 1000 == 0:
                                print 'yes'
                            if childd1.attrib['polarity'] == 'POS':
                                if childd2.attrib['polarity'] == 'POS':
                                    A += 1
                                else:
                                    C += 1
                                    f2.write(childd1.text + '\n')
                            else:
                                if childd2.attrib['polarity'] == 'POS':
                                    B += 1
                                    f1.write(childd1.text + '\n')
                                else:
                                    D += 1
                            break
                break
print A, B, C, D
print 'pos'
p1 = A / (A + C)
r1 = A / (A + B)
print 'precision:'
print p1
print 'recall'
print r1
print 'f'
print 2 * p1 * r1 / (p1 + r1)
print 'neg'
p2 = D / (B + D)
r2 = D / (C + D)
print 'precision:'
print p2
print 'recall'
print r2
print 'f'
print 2 * p2 * r2 / (p2 + r2)
print 'accuracy:'
print (A + D) * 1.0 / (A + B + C + D)

# vim: sw=4 ts=4 sts=4 expandtab

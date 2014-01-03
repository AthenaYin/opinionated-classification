#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from features import getfeatures
from svm import getopn
import os


RAW_FILES = os.listdir('newtestdata/')


cc = 0
for filename in RAW_FILES:
    print 'in execute.py ' + filename
    tree = ET.parse('newtestdata/' + filename)
    root = tree.getroot()
    for child in root:
        for childd in child:
            if childd.tag != 'sentence':
                continue
            if childd.text is None:
                continue
#            print childd.text
            wlist = getfeatures(childd.text)
#            print wlist[0]
            if getopn(wlist):
                childd.attrib['polarity'] = 'POS'
            else:
                childd.attrib['polarity'] = 'NEG'
            cc += 1
    tree.write('bayesans/' + filename)

print cc



# vim: sw=4 ts=4 sts=4 expandtab

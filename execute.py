#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from features import getfeatures
from svm import getopn
import os


RAW_FILES = os.listdir('ans/')


cc = 0
for filename in RAW_FILES:
    print 'in execute.py ' + filename
    tree = ET.parse('ans/' + filename)
    root = tree.getroot()
    for child in root:
        for childd in child:
            if childd.tag != 'sentence':
                continue
            cc += 1
            if childd.text is None:
                childd.attrib['polarity'] = 'NEG'
                continue
            wlist = getfeatures(childd.text)
            if getopn(wlist):
                childd.attrib['polarity'] = 'POS'
            else:
                childd.attrib['polarity'] = 'NEG'
    tree.write('svmans/' + filename)

print cc



# vim: sw=4 ts=4 sts=4 expandtab

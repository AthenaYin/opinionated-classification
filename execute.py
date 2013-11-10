#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from features import getfeatures
from svm import getopn
import os


RAW_FILES = os.listdir('rawdata/')


for filename in RAW_FILES:
    print 'in execute.py ' + filename
    tree = ET.parse('rawdata/' + filename)
    root = tree.getroot()
    for child in root:
        for childd in child:
            if childd.tag != 'sentence':
                continue
            if childd.text is None:
                childd.attrib['opinionated'] = 'N'
                continue
            wlist = getfeatures(childd.text)
            if getopn(wlist):
                childd.attrib['opinionated'] = 'Y'
            else:
                childd.attrib['opinionated'] = 'N'
    tree.write('svmans/' + filename)



# vim: sw=4 ts=4 sts=4 expandtab

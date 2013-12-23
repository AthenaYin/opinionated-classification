#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from features import getfeatures
from count import getopn
import os


RAW_FILES = os.listdir('ans/')


for filename in RAW_FILES:
    print 'in execute.py ' + filename
    tree = ET.parse('ans/' + filename)
    root = tree.getroot()
    for child in root:
        for childd in child:
            if childd.tag != 'sentence':
                continue
            if childd.text is None:
                childd.attrib['polarity'] = 'NEG'
                continue
            wlist = getfeatures(childd.text)
            if getopn(wlist):
                childd.attrib['polarity'] = 'POS'
            else:
                childd.attrib['polarity'] = 'NEG'
    tree.write('count1ans/' + filename)



# vim: sw=4 ts=4 sts=4 expandtab

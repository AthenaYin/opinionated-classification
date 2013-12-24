#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import xml.etree.ElementTree as ET

pol = []
f = open('pol.txt')
for line in f:
    pol.append(line)
f.close()
i = 0
root = ET.Element("Result")
f = open('newcorpus.txt')
for line in f:
    array = ET.SubElement(root, "weibo")
    array.attrib['id'] = "%d" % i
    sentence = ET.SubElement(array, "sentence")
    sentence.attrib['id'] = "%d" % i
    try:
        sentence.text = line.decode('utf-8')
    except:
        print line
        continue
    if pol[i] == 1:
        sentence.attrib['polarity'] = 'POS'
    elif pol[i] == -1:
        sentence.attrib['polarity'] = 'NEG'
    i += 1
f.close()
tree = ET.ElementTree(root)
tree.write("cities.xml", encoding="UTF-8")

#vim: ts=4 sw=4 sts=4 expandtab

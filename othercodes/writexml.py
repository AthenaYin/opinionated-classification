#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import xml.etree.ElementTree as ET

pol = []
f = open('pol.txt')
for line in f:
    line = line.strip();
    pol.append(line)
f.close()
i = -1
c = 0
root = ET.Element("Result")
f = open('newcorpus.txt')
for line in f:
    i += 1
    if i < 2000:
      continue
    array = ET.SubElement(root, "weibo")
    array.attrib['id'] = "%d" % i
    sentence = ET.SubElement(array, "sentence")
    sentence.attrib['id'] = "%d" % i
    try:
        sentence.text = line.decode('utf-8')
    except:
        print line
        continue
    if pol[i] == '1':
        c += 1
        sentence.attrib['polarity'] = 'POS'
    elif pol[i] == '-1':
        c += 1
        sentence.attrib['polarity'] = 'NEG'
f.close()
print c
tree = ET.ElementTree(root)
tree.write("testdata.xml", encoding="UTF-8")

#vim: ts=4 sw=4 sts=4 expandtab

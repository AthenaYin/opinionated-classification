#!/usr/bin/env python1.6
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

rootnew = ET.Element('Result')
filelist = ['../newtraindata/traindata.xml', '../newtestdata/testdata.xml']
i = 0
for filename in filelist:
	tree = ET.parse(filename)
	root = tree.getroot()
	for child in root:
		array = ET.SubElement(rootnew, 'weibo')
		array.attrib['id'] = child.attrib['id']
		for childd in child:
			if not childd.attrib.has_key('polarity'):
				continue
			i += 1
			sentence = ET.SubElement(array, 'sentence')
			sentence.attrib['polarity'] = childd.attrib['polarity']
			sentence.text = childd.text
tree = ET.ElementTree(rootnew)
tree.write('mergedata.xml', encoding = 'UTF-8')
print i

#!/usr/bin/env python1.6
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET


tree = ET.parse('mergedata.xml')
root = tree.getroot()
count = 0
count2 = 0
rootnew = ET.Element('Result')
treenew = ET.Element(rootnew)
filename = "%d" % count2
for child in root:
	if count == 4501:
		break
	if count2 == 0 and count == 0:
		count2 = 1
		filename = "%d" % count2
		filename = 'test/' + filename + '.xml'
	elif count % 900 == 0 and count != 0:
		treenew = ET.ElementTree(rootnew)
		treenew.write(filename, encoding = 'UTF-8')
		#write to fil
		count2 += 1
		print count2
		print count
		rootnew = ET.Element('Result')
		treenew = ET.Element(rootnew)
		filename = "%d" % count2
		filename = 'test/' + filename + '.xml'
		count = 0
	else:
		tmp = 0
		for childd in child:
			if not childd.attrib.has_key('polarity'):
				continue
			count += 1
			array = ET.SubElement(rootnew, 'weibo')
			array.attrib['id'] = child.attrib['id']
			sentence = ET.SubElement(array, 'sentence')
			sentence.attrib['id'] = "%d" % count
			sentence.attrib['polarity'] = childd.attrib['polarity']
			sentence.text = childd.text

	

#!/usr/bin/env python1.6
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from features import getfeatures

tree = ET.parse('newtraindata/traindata.xml')
root = tree.getroot()
i = 0
for child in root:
	for childd in child:
		if not childd.attrib.has_key('polarity'):
			continue
		mlist = getfeatures(childd.text)
		if mlist[0] == 0:
			del childd.attrib['polarity']
		else:
			i += 1
print i
tree.write('test/traindata.xml')


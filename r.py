#!/usr/bin/env python1.6
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from features import getfeatures


def readxml(namexml, numofsen):
    tree = ET.parse(namexml)
    root = tree.getroot()
    slist = []
    print root.tag
    for child in root:  # traverse every weibo
        for childd in child:  # traverse every sentence
            if childd.tag != 'sentence':
                continue
            flag = 0
            for st in childd.attrib:
                if st == 'polarity':
                    flag = 1
            if flag == 0:
                continue
            mlist = getfeatures(childd.text)  # for every sentence in the xml, get their feature to form a feature vector
            print childd.attrib['polarity']
            if childd.attrib['polarity'] == 'POS':
                mlist.append(1)
            else:
                mlist.append(0)
            slist.append(mlist)
            numofsen[0] += 1
    return slist


# vim: sw=4 ts=4 sts=4 expandtab

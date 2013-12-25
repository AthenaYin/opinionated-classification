#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import sys
import re

with open('corpus.txt') as f:
    i = 0
    for line in f:
        i += 1
        senpol, rest = line.strip().split('\t')[:2]
        rest = rest.strip()
        rest = re.sub(r'\/{1,2}[a-z]{1,100}[ ]{0,1}', '', rest)
        rest = re.sub('<.*?>', '', rest)
        try:
            print rest.decode('utf-8').encode('utf-8')
        except Exception, e:
            print >> sys.stderr, e, rest, "Error"
# vim: ts=4 sw=4 sts=4 expandtab

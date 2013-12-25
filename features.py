#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#import jieba
import re
import sys
import os


"""
1.this function aims at finding the positive sentimental word in a sentence
"""


def senword(wordlist):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    for fname in ('negsen.txt', 'possen.txt', 'negest.txt', 'posest.txt',):
        f = open(os.path.dirname(os.path.abspath(__file__)) + '/senword/' + fname, 'r')
        for line in f:
            line = line.strip()
            if len(line) > 3 and line in wordlist:  # ignore one-character word in the wordnet
                return 1
        f.close()
    return 0


"""
2.this function examines whether the sentence has some pronouns
"""


def pronoun(wordlist):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    for line in (u'你们', u'我们', u'我', u'你'):
        if line in wordlist:
            return 1
    else:
        return 0


"""
3.this function examines whether there is some wrong-used exclamation marks
"""


def claims(wordlist):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    if (wordlist.count(u'！') > 1) or (wordlist.count(u'？') > 1):
        return 1
    else:
        return 0


"""
4.this file examines if there exist only one '!' or '?' or both
"""


def claim(wordlist):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    if (wordlist.count(u'！') == 1) or (wordlist.count(u'？') == 1):
        return 1
    else:
        return 0


"""
5.this file examines if theres any exclamation words together with '！' and '？'
"""


def claimword(wordlist):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    if claim(wordlist) == 0:
        return 0
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/senword/claimword.txt', 'r')
    for line in f:
        line = line.strip()
        if len(line) and line in wordlist:
            return 1
    f.close()
    return 0


"""
6.examines if there are any words presenting standpoint
"""


def opinion(wordlist):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/senword/stand.txt', 'r')
    for line in f:
        line = line.strip()
        if len(line) > 3 and line in wordlist:
            return 1
    return 0


"""
7.examines if there's digit
"""


def digit(wordlist):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    for i in range(0, len(wordlist)):
        if wordlist[i].isdigit():
            return 1
    return 0

"""
8.examines if there's any negation words
"""


def negword(wordlist):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    for fname in ('negationw.txt', ):
        f = open(os.path.dirname(os.path.abspath(__file__)) + '/senword/' + fname, 'r')
        for line in f:
            line = line.strip()
            if line in wordlist:  # ignore one-character word in the wordnet
                return 1
        f.close()
    return 0


"""
9.examines if there's any adj
"""


def exword(wordlist):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    for fname in ('extent.txt', ):
        f = open(os.path.dirname(os.path.abspath(__file__)) + '/senword/' + fname, 'r')
        for line in f:
            line = line.strip()
            if len(line) > 3 and line in wordlist:  # ignore one-character word in the wordnet
                return 1
        f.close()
    return 0

"""
10. word expressing blessings
"""


def wishword(wordlist):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    for w in (u'祝福', u'祝愿', u'但愿', u'希望', u'愿望'):
        if w in wordlist:  # ignore one-character word in the wordnet
                return 1
    return 0


def numsenword(mlist, wordlist):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    cc = 0.0
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/senword/' + 'newnegsen.txt', 'r')
    for line in f:
        line = line.strip()
        if len(line) > 3 and line in wordlist:
            print line
            cc += -wordlist.count(line)
            mlist.append(1)
        else:
            mlist.append(0)
    f.close()
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/senword/' + 'newpossen.txt', 'r')
    for line in f:
        line = line.strip()
        if len(line) > 3 and line in wordlist:
            print line
            cc += wordlist.count(line)
            mlist.append(1)
        else:
            mlist.append(0)
    f.close()
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/senword/' + 'NewNewPosSen.txt', 'r')
    for line in f:
        line = line.strip()
        if line in wordlist:
            print line
            cc += wordlist.count(line)
            mlist.append(1)
        else:
            mlist.append(0)
    f.close()
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/senword/' + 'NewNewNegSen.txt', 'r')
    for line in f:
        line = line.strip()
        if line in wordlist:
            print line
            cc += -wordlist.count(line)
            mlist.append(1)
        else:
            mlist.append(0)
    f.close()
    return cc

def getfeatures(sen):
    try:
        sen = re.sub(r'#.*#', '', sen)
    except:
        print repr(sen)
        raise
    sen = sen.strip()
#    sen = '|'.join(jieba.cut(sen))
    mlist = []
    tmp = []
    numsenword(mlist, sen)
#    mlist.append(numsenword(tmp, sen))
#    mlist.append(senword(sen))
#    mlist.append(pronoun(sen))
#    mlist.append(claims(sen))
#    mlist.append(claim(sen))
#    mlist.append(claimword(sen))
#    mlist.append(opinion(sen))
#    mlist.append(digit(sen))
#    mlist.append(negword(sen))
#    mlist.append(exword(sen))
#    mlist.append(wishword(sen))
    return mlist

# vim: sw=4 ts=4 sts=4 expandtab

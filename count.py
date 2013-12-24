#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from r import readxml
import os
import random


def getopn(wlist):
	if wlist[0] > 0.0:
		return 1
	elif wlist[0] < 0.0:
		return 0
	else:
		return random.choice([0, 1])

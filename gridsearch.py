#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import os
from r import readxml
from sklearn.cross_validation import KFold
from sklearn import svm, grid_search


NOF = 34
numofsen = []
numofsen.append(0)
vecfeature = []
for filename in os.listdir('traindata/'):
    print 'in gridsearch.py ' + filename
    vecfeature += readxml('traindata/' + filename, numofsen)
X = []
y = []
for line in vecfeature:
    X.append(line[:-1])
    y.append(line[NOF])
kf = KFold(len(y), n_folds=10)
para = []
i = 1.0
for i in range(1, 5):
    mi = -1 + 0.5 * i
    ans = 2 ** mi
    para.append(ans)
param_grid = {'C': para, 'gamma': para, 'kernel': ['rbf']}
svr = svm.SVC()
clf = grid_search.GridSearchCV(svr, param_grid, cv=kf)
clf.fit(X, y)
print clf.best_params_

# vim: sw=4 ts=4 sts=4 expandtab

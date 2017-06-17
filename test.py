#!usr/bin/env python
#-*- coding: utf-8 -*-
import numpy as np
from sklearn.datasets import load_svmlight_file
import math
import sys
import os
from math import log
import operator

train_X,train_y=load_svmlight_file('train.scale')
train_x=train_X.toarray() 

def calcShannonEnt(dataSet,labelset):
    numEntries = len(dataSet)
    labelCounts = {}
    for laVec in labelset:
        currentLabel = laVec
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt
        
print calcShannonEnt(train_x,train_y)
     



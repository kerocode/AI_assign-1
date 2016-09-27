
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt

import fileinput

f = fileinput.input('data.txt')
_male = []
_female = []
_target = []
X = []
Y = []
for line in f:
    temp = line.split(",")
    if str(temp[2]) == '0\n' :
        X.append([round(float(temp[0]),2), round(float(temp[1]),2)])
        Y.append(0)
    else:
        X.append([round(float(temp[0]), 2), round(float(temp[1]), 2)])
        Y.append(1)

clf = svm.SVC(kernel='linear', C = 1.0)

clf.fit(X,Y)


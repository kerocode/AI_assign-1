import matplotlib.pyplot as plt
import numpy as np
_fheight = np.random.normal(50, 6, 2000)
_mheight = np.random.normal(85, 8, 2000)
_fheight = np.sort(_fheight)
_mheight = np.sort(_mheight)
_mweight = np.random.normal(175, 21, 2000)
_fweight = np.random.normal(180, 23, 2000)
f = open('data.txt', 'w')

for a in range(0,2000, 1):
    _mheight[a] = round(_mheight[a],1)
    _mweight[a] = round(_mweight[a],1)
    _fweight[a] = round(_fweight[a],1)
    _fheight[a] = round(_fheight[a],1)
    f.write(str(_mheight[a]))
    f.write(',')
    f.write(str(_mweight[a]))
    f.write(', 0\n')
    f.write(str(_fheight[a]))
    f.write(',')
    f.write(str(_fweight[a]))
    f.write(', 1\n')

f.close()

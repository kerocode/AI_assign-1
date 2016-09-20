
import matplotlib.pyplot as plt
import fileinput

f = fileinput.input('data.txt')
_m_weight = []
_m_height = []
_f_weight = []
_f_height = []
for line in f:
    temp = line.split(",")
    if str(temp[2]) == '0\n' :
        _m_height.append(round(float(temp[0]),2))
        _m_weight.append(round(float(temp[1]),2))
    else:
        _f_height.append(round(float(temp[0]),2))
        _f_weight.append(round(float(temp[1]),2))


'''
# blue is female
plt.plot(_f_height,_f_weight, 'bo')
#red is male
plt.plot(_m_height,_m_weight, 'ro')
plt.ylabel("weight")
plt.xlabel("height")

plt.show()
'''

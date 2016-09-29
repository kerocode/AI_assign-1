
import matplotlib.pyplot as plt
import fileinput
import numpy as np

f = fileinput.input('data.txt')
_m_weight = []
_m_height = []
_f_weight = []
_f_height = []

#height for male and female
feature_A = []
#weight for male and female
feature_B = []
# labels 0 for male and 1 for female
labels = []
for line in f:
    temp = line.split(",")
    if str(temp[2]) == '0\n' :
        feature_A.append(round(float(temp[0]),2))
        feature_B.append(round(float(temp[1]),2))
        labels.append(0)
    else:
        feature_A.append(round(float(temp[0]),2))
        feature_B.append(round(float(temp[1]),2))
        labels.append(1)
# blue is female male is red
colormap = np.array(['r', 'b'])
print  len(labels) , len(feature_B) , len(feature_A)

#plt.scatter(range(len(feature_A)),feature_A,c=colormap[labels] )
plt.scatter(range(len(feature_A)),feature_A , c=colormap[labels])
plt.show()

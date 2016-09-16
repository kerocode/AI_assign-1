import matplotlib.pyplot as plt
import fileinput

f = fileinput.input('female.txt')
_weight = []
_height = []
for line in f:
    temp = line.split(",")
    _height.append(round(float(temp[0]),2))
    _weight.append(round(float(temp[1]),2))



plt.plot(_height,_weight, 'ro')
plt.ylabel("female-weight")
plt.xlabel("female-height")

plt.show()


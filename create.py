import  random
from math import ceil
import fileinput
import shlex


'''import fileinput
'''
new_male = open("nfemale.txt","w")
f = fileinput.input('female.txt')

for line in f:
    new_line = ",".join(shlex.split(line))
    new_male.write(new_line + ',1\n')

f.close()
'''

for i in range(2000):
    _m_height = random.uniform(4,6.4)
    _m_weight = random.uniform(95,280)
    _m_height = round(_m_height,2)
    _m_weight = round(_m_weight,2)
    _male = str(_m_height) + "," + str(_m_weight) + "," + "0\n";
    _f_height = random.uniform(3.5,5.8)
    _f_weight = random.uniform(85,310)
    _f_height = round(_f_height,2)
    _f_weight = round(_f_weight,2)
    _female = str(_f_height) + "," + str(_f_weight) + "," + "1\n";
    female.write(_female)
    male.write(_male)
'''

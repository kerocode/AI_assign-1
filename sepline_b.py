
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import perceptron
from pandas import *
import fileinput

f = fileinput.input('data.txt')

#height of females and males
X_1 = []
#weight of female and males
X_2 = []
#labels 0 males and 1 females
Y = []
for line in f:
    temp = line.split(",")
    if str(temp[2]) == '0\n' :
        X_1.append(round(float(temp[0]),2))
        X_2.append(round(float(temp[1]),2))
        Y.append(0)
    else:
        X_1.append(round(float(temp[0]), 2))
        X_2.append(round(float(temp[1]), 2))
        Y.append(1)

print len(X_1)
print len(Y)
inputs = DataFrame({
'Height' : X_1,
'Weight' : X_2,
'Targets' : Y
})
colormap = np.array(['r', 'b'])


net = perceptron.Perceptron(n_iter=1000, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)

# Train the perceptron object (net)
net.fit(inputs[['Height','Weight']],inputs['Targets'])
# calculate  TP  FP TN FN
def perf_measure(y_actual, y_hat):
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    for i in range(len(y_hat)):
        if y_actual[i]== y_hat[i]==1:
           TP += 1
        elif y_actual[i]==1 and y_actual!=y_hat[i]:
           FP += 1
        elif y_actual[i]==y_hat[i]==0:
           TN += 1
        elif y_actual[i]==0 and y_actual!=y_hat[i]:
           FN += 1

    return( "TP :" + str(TP) , "FP :" + str(FP), "TN :" + str(TN), "FN :" + str(FN))
# Output the values
print "Coefficient 0 " + str(net.coef_[0, 0])
print "Coefficient 1 " + str(net.coef_[0, 1])
print "Bias " + str(net.intercept_)
# Do a prediction
pred = net.predict(inputs[['Height','Weight']])
score = net.score(inputs[['Height','Weight']],inputs['Targets'])
print "accuracy : " + str(score *100 )  + "%"
print  "error :"  + str((1- score)*100) + "%"


#print perf_measure(Y,pred)
from sklearn.metrics import confusion_matrix
print confusion_matrix(pred, inputs['Targets'])


plt.scatter(inputs.Height,inputs.Weight, c=colormap[inputs.Targets],s=20)

plt.show()




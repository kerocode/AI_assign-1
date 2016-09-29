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

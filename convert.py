import fileinput
data = open("data.txt", 'w')
f = fileinput.input(files=('nfemale.txt ', 'nmale.txt'))



# convert kg to lb
def kgTolb(kg):
    return  round ((float(kg)/ 0.45359237), 2)
#convert cm to foot
def cmToft(cm):
    return  round ((float(cm)* 0.0328084),2)

for line in f :
    tem = line.split(",")
    height = cmToft(tem[0])
    weight = kgTolb(tem[1])
    gander = tem[2]
    print gander
    data.write(str(height) +','+str(weight)+','+str(gander) )
f.close()


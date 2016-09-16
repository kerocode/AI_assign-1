import fileinput
data = open("data.txt", 'w')
f = fileinput.input(files=('female.txt ', 'male.txt'))

for line in f :
    data.write(line)
f.close()

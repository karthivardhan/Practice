f = open('test.txt')
line = f.readline()
while line!="":  # line not equal to empty
    print(line)
    line = f.readline()
f.close()
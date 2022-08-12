# Read number of line using readlines method and loop
file = open('test.txt')

for line in file.readlines():
    print(line)
file.close()
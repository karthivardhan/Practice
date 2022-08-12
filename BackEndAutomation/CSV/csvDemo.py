import csv

with open('/Users/apparaojajimoggala/PycharmProjects/Envelope Report.csv') as csvFile:
    # csv.reader() method helps to read the content of the file
    csvReader = csv.reader(csvFile, delimiter=',')
    #print(csvReader)
    #print(list(csvReader))
    Date = []
    Time = []
    for column in csvReader:
        Date.append(column[1:])
        Time.append(column[1:])
print(Date)
print(Time)



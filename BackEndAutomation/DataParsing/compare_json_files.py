import json

with open('/Users/apparaojajimoggala/PythonSelenium notes/test.json') as file:
    data1 = json.load(file)

with open('/Users/apparaojajimoggala/PythonSelenium notes/test2.json') as file:
    data2 = json.load(file)

    print(data1 == data2) # False


# When more keys with same name and wanted to get one key value without indexing
import json

with open('/Users/apparaojajimoggala/PythonSelenium notes/test2.json') as file:
    data = json.load(file)
    print(data)
    data2 = data['WEEK'][0]['EXPENSE']
    print(type(data2))
    print(data2)
    for w in data['WEEK'][0]['EXPENSE']:
        print(w)
    if w['WHAT'] == 'Car':
        print(w['AMOUNT']) # 20
        assert w['AMOUNT'] == 20

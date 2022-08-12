# Parse content from Json file

import json

with open('/Users/apparaojajimoggala/PythonSelenium notes/test.json') as file:
    data = json.load(file)
    print(data)
    print(type(data))
    print(data['eBooks'][1])
    print(type(data['eBooks'][1]))
    print(data['eBooks'][1]['language']) #Python
    for books in data['eBooks']:
        print(books)
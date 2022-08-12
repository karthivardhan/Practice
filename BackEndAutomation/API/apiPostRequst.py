import json

import requests
import configparser  # this is to import .ini file


# post(url, data, json, params, headers, cookies)
config = configparser.ConfigParser()
config.read('Utilities/properities.ini') # read the file
post_req = requests.post(config['API']['endpoint']+'/Library/Addbook.php', json={
    "name": "Python Scripting",
    "isbn": "RS531456991654",
    "aisle": "1596",
    "author": "Karthikeya Jajimoggala"
}, headers={"Content-Type" : "application/json"},)

assert post_req.status_code == 200

print(post_req.json())
json_res = post_req.json()
bookId = json_res['ID']
print(bookId)

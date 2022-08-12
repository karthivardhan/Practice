import requests
from payload import *
from Utilities.properties import *


url = endpoint+add
query = 'select * from Books'
headers = {"Content-Type": "application/json"}
post_req = requests.post(url, json=buildPayloadFromDB(query), headers=headers,)

res_json = post_req.json()
print(res_json)

#bookId = res_json['ID']

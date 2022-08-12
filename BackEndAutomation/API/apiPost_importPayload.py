import requests
from payload import *
from Utilities.properties import *
# import configparser  # this is to import .ini file


# Send a new value to 'isbn' parameter via method instead via payload
# config = configparser.ConfigParser()  # method
# config.read('Utilities/properities.ini')  # to read the file

url = endpoint+add
headers = {"Content-Type": "application/json"}
post_req = requests.post(url, json=addBook('newab2c14569'), headers=headers,)

assert post_req.status_code == 200
print(post_req.json())

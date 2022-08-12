import requests
from Utilities.properties import *

url = endpoint+deleteBook
delete_book = requests.delete(url, json={"ID": "newab1456915964"}, )

print(delete_book.json())
assert delete_book.status_code == 200

json_res = delete_book.json()
print(json_res["msg"])
assert json_res["msg"] == "book is successfully deleted"

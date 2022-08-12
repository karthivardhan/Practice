# Environmental Controls
# The environment.py module may define code to run before and after certain events during your testing:


import requests
from steps.properties import *

def after_scenario(context, scenario):
    url = endpoint+deleteBook
    delete_book = requests.delete(url, json={"ID": context.bookId}, )  # bookId will be coming from .feature file
    print(delete_book.json())
    assert delete_book.status_code == 200
    json_res = delete_book.json()
    print(json_res["msg"])
    assert json_res["msg"] == "book is successfully deleted"
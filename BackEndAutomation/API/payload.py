from Utilities.configurations import *

def addBook(isbn):
    book = {
        "name": "Python Scripting Book New Edition",
        "isbn": isbn,
        "aisle": "15964",
        "author": "Karthikeya Jajimoggala"
    }
    return book

# Crete empty dict and adding key value pairs, add values from DB
def buildPayloadFromDB(query):
    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody

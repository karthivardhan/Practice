import mysql.connector

from Utilities.properties import *
def getPassword():
    password = 'jAji@059049'
    return password


'''connect_config = {
    'user': userName,
    'password': password,
    'localhost': hostName,
    'APIDevelop': databaseName,
}'''

# Connect to DB and execute query
def getQuery(query):
    con = mysql.connector.connect(host=hostName, database=databaseName,
                                  user=userName, password=password)
    cur = con.cursor()  # cursor method helps to form streamline connection between Python and DB to talk to DB table
    cur.execute(query)  # execute method helps to execute sql queries
    row = cur.fetchone()
    con.close()
    return row


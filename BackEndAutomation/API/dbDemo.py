import mysql.connector
from Utilities.properties import *
from mysql.connector import Error

# host, database name, user, password
# localhost -> if its installed in local machine
try:  # TRY CATCH to check whether its connected or not with logs
    con = mysql.connector.connect(host=hostName, database=databaseName,
                                  user=userName, password=password)  # this method helps to connect the database
    if con.is_connected():
        print('connected successfully')
except Error as e:
    print(e)

print(con.is_connected())  # return True if its connected successfully

cur = con.cursor()  # cursor method helps to form streamline connection between Python and DB to talk to DB table
cur.execute('select * from CustomerInfo;')  # execute method helps to execute sql queries
row = cur.fetchone()  # fetch helps to fetch the details from table. fetchone() method fetch the first row details
print(row)  # returns in Tuple
print(row[3])

rows = cur.fetchall()
print(rows)  # returns in list (list of Tuples)
print(rows[1])

# return all the amounts from column
sum = 0
for r in rows:
    print(r[2])  # amount is 3rd column
    sum = sum + r[2]  # add all amounts
print(sum)
assert sum == 241

# Update a row value
cur.execute("update customerInfo set Location = 'Canada' where CourseName = 'Jmeter';")
con.commit()  # to commit the changes into DB

# Without hard coding the values
query = "update customerInfo set Location = %s where CourseName = %s;"  # replace with %s
data = ('Australia', 'Jmeter')
cur.execute(query, data)
con.commit()  # 'Australia' will be updated in place of 'Canada'

# Similarly, we can also delete and insert values into DB table

con.close()  # to close connection

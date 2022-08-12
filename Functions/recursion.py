# Recursion:-  function calling itself is called recursion.
# By default it will print 1000 times
# But we can set our own value how many number of times

import sys # default function
sys.setrecursionlimit(2000)
def great():
    print('Hello')
    great() # calling function itself
great()
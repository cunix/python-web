# !-_- coding:utf-8 +_+!
"This is a practice about json"


"""
Json  ---->   Python
object        dict
array         list
str           unicode str
number(int)   int, long
number(real)  float
true          True
false         False
null          None
-----------------------------
Python ---->   Json
dict           object
list,tuple     array
unicode str    str
int, long      number(int)
float          number(real)
True           true
False          false
None           null
"""


import json
s=[{"f":(1,2,3),"x":None},{"f":(1,2,3),"x":None},{"f":(1,2,3),"x":None},{"f":(1,2,3),"x":None}]
# list to json
d=json.dumps(s)


print d
# json to list
l=json.loads(d)
print l



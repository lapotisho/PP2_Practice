import json
from math import *

json_string = '''{ "students":[{"id":1,"name":"Tim","age":21,"full-time":true},{"id":2,"name":"Joe","age":33,"full-time":false}]}'''
data = json.loads(json_string) # it reads and parses into a dictionary
data["key"] = 123
data["key2"] = "Timo"
print(type(json_string))
print(type(data))
print(data)
print(json_string)
print(data.get("students"))
new_json = json.dumps(data) # inserts elements into a new json string
print(new_json)
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# x is a dict 
y = json.dumps(x) # y becomes a json string with values of x
print(y)
a = []
i = 1 
while i <= 10:
    a.append(i)
    i+=1  
x["array"] = a
y = json.dumps(x)
a = (2,3,1,4,5)
x["tuple"] = a
y = json.dumps(x)
x["number"] = 67
x["float"] = pi
y = json.dumps(x)
print(type(y))
print(y)
print(type(x))
print(x)
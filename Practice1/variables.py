l = "awesome"

def myfunc():
  print("Python is " + l)
  
myfunc()
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
a = "Python"
b = "is"
c = "awesome"
print(x, y, z)
print(67)
print("six seven")
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))
x = 1
y = 3565622255
z = -325
print(type(x))
print(type(y))
print(type(z))
x = 1.10
y = 1.0
z = -35.5
print(type(x))
print(type(y))
print(type(z))
x = 35e3
y = 12E4
z = -87.7e10
print(type(x))
print(type(y))
print(type(z))
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1, 10))
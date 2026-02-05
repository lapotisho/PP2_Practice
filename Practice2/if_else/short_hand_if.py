# syntax result = a if condition else b
x = 100 
v = "big" if x > 100 else "tiny" #v is already in if True clause , after else is the second value of v
print(v)
a = 10 
b = 19
result , mini = ("a is bigger",'b') if a > b else ("b is greater",'a') # we can declare several values in short hand if by allocating by the end for example a,b,...n = ( m1,m2,m3,...m ) if condition else (y1,y2,y3,...y)
print(result,"than",mini)
a="hello"
b ="Hello!"
print('a is longer than b') if len(a) > len(b) else print("b is longer than a")
username=input() 
display_name = username if len(username) != 0 else "no valid username"
print("welcome,",display_name) if display_name != "no valid username" else print(display_name)
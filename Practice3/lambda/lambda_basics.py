x = int(input())
xr = lambda x : x*x # this is a power function 
print(type(xr)) # we will get type of function 
print(xr(x))
a,b = map(int,input().split())
suma = lambda x,y: x+y # this is a sum function through lambda function 
print(suma(a,b))
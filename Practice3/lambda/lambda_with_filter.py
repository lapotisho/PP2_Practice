from math import sqrt
a = [1,2,3,4,5,6,7,8,9]
even = filter(lambda x:x%2==0,a)
odd = filter(lambda x:x%2!=0,a)
print(type(even))
print(list(even))
print(list(odd))
a=[]
x = 1
while x <= 100: # making a list of 100 numbers
    a.append(x)
    x+=1 
power = list(filter(lambda x: sqrt(x).is_integer() ,a))
print(power) # it will print only numbers with power of two 
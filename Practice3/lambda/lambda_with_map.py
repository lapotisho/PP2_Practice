a = ["bonana","apple","pineapple"]
b = ['1','2','3']
c= ["coconut","lychee","eggplant"]
x = [1,2,3]
y = [9,8,7]
result = map(lambda x,y: x+y,a,b)
print(list(result))
result = map(lambda x,y: x+y,x,y)
print(list(result))
result = map ( lambda askom,cook: askom*cook,x,y)
print(set(result))
result = map(lambda a,b:a+b,a,c)
print(type(result)) # data type is map which means every value in the var is an iterator
print(tuple(result))
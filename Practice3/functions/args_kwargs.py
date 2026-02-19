import sys
def d(*a): #recieves the whole list/tuple/set/etc
    print(x,end=" ") # it will print the values inside of the list with spaces 
a = ["Cat","Dog","Elephant"]
for x in a:
    d(a)
def t(*a):
    print(type(a))
print()
t() # *args or arbitrary(any number of ) arguments are tuple data type
mydic = { "county":"Kazakhstan", "city":"Almaty" , "street":"Fake St." , "education":"KBTU"}
def m(**kwargs): #recieves the whole dictionary
    for key,value in kwargs.items():
        print(f"{key}: {value}")
m(**mydic)
def all_(*a,**am):
    for x in a:
        print(x,end="~")
    print()
    for value in am.values():
        print(value,end=' ')
all_(*a,**mydic)
def order_pizza(size,*top):
    print(f"the size of a pizza is {size} and the following topings are ",end='')
    for x in top:
        print(x,end=" ")
print("large/small")
a=input("what size of pizza you want: ")
if a.lower() in "large" or a.lower() in "small": 
    print("what toppings you would like: ",end="") 
else: 
    print("invalid size, please try again")
    sys.exit() # this command will exit the whole program
b = list(map(str,input().split()))
order_pizza(a,*b)
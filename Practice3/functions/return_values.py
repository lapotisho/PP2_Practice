def summ(a,b): 
    return a + b # this will be a value of the function 
a = ["Bananas","apples","coconuts"]
b = ["Pineapples","pomegranats","Watermelon"]
result = map(summ,a,b)
print(list(result))
def fib(n): # this is a fibonacci sequence 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fib(n-2)+fib(n-1)
n = int(input())
for x in range(n): 
    print(fib(x),end=" ")
def even(y):
    return y % 2 == 0

a = []
i = 1
while i <= 100:
    a.append(i)
    i += 1

a = list(filter(even,a)) # it will filter all even numbers
print(a)
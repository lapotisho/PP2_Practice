from math import * 
#i import all possible libraries in the module math

x = 1.1
x = ceil(x)
print(x)
y = 12.999999
print(floor(y))
x = 10 # people
y = 6 # seats 
# i'll use basic combinatorics' combination formula
print(comb(x,y)) # greater number goes first according to the formula c = n!/r!(n-r)! in this case it's 210 possible combinations
print(perm(x,y)) # permutations but the elements' pos don't matter so this value will be much bigger than the first one
x,y=10,-8
print(abs(x*y))
print(fabs(x*y)) # the same as abs but returns float 
x = -100
a =[]
while x <= 100:
    a.append(x)
    x+=5 
print(sum(a))
print(min(a))
print(max(a))
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)
print(int(pow(y,x))) # 25^5
y = 2
x = 1
while x < 128:
    print(int(pow(y,x)),end=" ")
    x*=2
print("the last number is 64-bit")
x=int(input("Enter radius of a circle: "))
s = int(pow(x,2)) * pi
print(s)
print(ceil(s))
print(floor(s))
x=int(input("Enter any number below or equal 32: "))
print(factorial(x) if x <= 32 else "the value is very big try again")
print("\033[31menter only integers\033[0m")
x=int(input("Enter any number : "))
y=int(input("Enter any number : "))
print(f"this is the remainder of x divided by y : {int(fmod(x,y))}")
print(f"this is the GREATEST COMMON DIVISOR : {int(gcd(x,y))}")
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
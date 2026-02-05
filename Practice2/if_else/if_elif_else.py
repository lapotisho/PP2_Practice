x = 50
y = 67
if x > y: 
    print("x is greater than y")
else: 
    print("y is greater than x")

x = 67
y = 67
if x > y: 
    print("x is greater than y")
elif y < x : 
    print("y is greater than x")
elif y == x: 
    print("the are equal")

a = int(input()) # day of the week 

if a == 1: 
    print("monday") 
elif a == 2: 
    print("tuesday")
elif a == 3: 
    print("wednesday")
elif a == 4: 
    print("thursday")
elif a == 5: 
    print("friday")
elif a == 6: 
    print("saturday")
elif a == 7: 
    print("sunday")

a = 3 # day of the week 

if a == 1: 
    print("monday") 
elif a == 2: 
    print("tuesday") # it will execute only one true elif 
elif a == 3: 
    print("wednesday")
elif a == 4: 
    print("thursday")
elif a == 5: 
    print("friday")
elif a == 6: 
    print("saturday")
elif a == 7: 
    print("sunday")
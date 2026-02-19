def gmail(a):
    if len(a) > 0 and all( ch in "qwertyuiopasdfghjklzxcvbnm0123456789" for ch in a ):
            print(f"{a}@gmail.com")
    else: 
        print(" \033[91mInvalid name\033[0m")
def sum(a,b): #this is a sum function , it takes values i input then sum them and print
    print(a+b)
a,b=map(int,input().split())
sum(a,b)
a = input("Enter you name: ")
gmail(a)
def countdown(n): # this is a countdown recursive function
    if n == 0: 
        print("time is over")
    else: 
        print(n)
        countdown(n-1)
countdown(5) # the number inside of the function can be various but i chose 5 to not dump the terminal

with open("data.txt" , 'r' ) as f: 
    print(f.read())
n = input("What you want to add?: ")
with open('data.txt', 'a' ) as f: 
    f.write('\n'+n)
with open('data.txt' , 'r' ) as f:
    print(f.read())
f = open("myfile.txt", "x")
f.close()
f = open('myfile.txt', 'a')
f.write('this is a new file')
f.close() 
f = open('myfile.txt' , 'r' )
print(f.read())
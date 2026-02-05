a = 5
for x in range(1,10): 
    if a == x: 
        print()
        print("the loop ended at x = 5 ")
        break
    else: 
        print(x,end=" ")
for i in range(1, 10):
    if i == 2:
        continue
    if i == 7:
        break
    print(i,end=" ")

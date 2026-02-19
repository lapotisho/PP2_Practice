lol=[(123,3),(321,2),(231,1)]
sort_lol = sorted(lol,key=lambda x: x[1])
print(sort_lol)
pupils = [("Win", 25), ("MacOS", 22), ("Linux", 28)]
pupils = sorted(pupils,key=lambda x:x[1])
print(pupils)
l=["apple", "pie", "banana", "cherry","coconut"]
ll = sorted(l,key=lambda x:len(x)) 
print(ll)
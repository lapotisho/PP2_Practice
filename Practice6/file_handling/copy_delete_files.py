import os 
import shutil
a = input("name a new file: ")
a = a+'.txt'
with open(a,'x') as f: 
    pass
n = input(f"do you want to delete the file {a}? : yes/no ")
if n.lower() == "yes": 
    os.remove(a)
if os.path.exists(a): 
    print(f"the file {a} exists ")
else: 
    print("nothing was found")
source = "/Users/baitas27gmail.com/Python-basics/Practice6/copy.txt"
destination = "/Users/baitas27gmail.com/Python-basics/Practice6/file_handling/copy2.txt"
shutil.copyfile(source,destination)
with open(destination,'r') as f: 
    print(f.read())
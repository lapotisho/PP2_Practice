import os
import shutil
l = list()
os.mkdir("this_is_a_folder")
with open('a.txt','x') as f:
    l.append('a.txt')
with open('b.txt','x') as f:
    l.append('b.txt')
with open('c.txt','x') as f:
    l.append('c.txt')
for ff in l:
    shutil.move(ff,"/Users/baitas27gmail.com/Python-basics/Practice6/directory_management/this_is_a_folder")
print(os.listdir("this_is_a_folder"))
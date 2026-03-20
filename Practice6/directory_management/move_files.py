import os 
import shutil
if not os.path.exists("new_folder"):
    os.mkdir("new_folder")
    os.mkdir("nested_folder")
with open("new_file.txt" , 'x' ) as f:
    pass 
with open("new_file.txt" , 'a' ) as f: 
    f.write("This is a new file inside of a new directory")
print( os.getcwd() )
shutil.move('new_file.txt',"/Users/baitas27gmail.com/Python-basics/Practice6/directory_management/new_folder")
shutil.move("/Users/baitas27gmail.com/Python-basics/Practice6/directory_management/new_folder","/Users/baitas27gmail.com/Python-basics/Practice6/directory_management/nested_folder")
with open("new_file2.txt" , 'x' ) as f:
    pass 
shutil.move("new_file2.txt","/Users/baitas27gmail.com/Python-basics/Practice6/directory_management/nested_folder")
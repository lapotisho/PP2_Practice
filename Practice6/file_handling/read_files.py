import os 
print(os.getcwd())
with open('data_for_reading.txt' , 'r' ) as f: 
    print(f.readline(),end='')
    print(f.readline())
with open('/Users/baitas27gmail.com/Python-basics/Practice6/new_data.txt','r') as f: 
    print(f.read())
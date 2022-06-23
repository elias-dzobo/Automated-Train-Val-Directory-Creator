import os 

root = './'

for subdirs, dirs, files in os.walk(root):
    print(len(os.listdir(subdirs))) 

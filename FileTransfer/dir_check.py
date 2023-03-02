import os
from os import walk
path =("C:\\CSU23021\\Comp_Networks_Project_2\\FileTransfer")
directorlist=os.listdir(path)

#print(directorlist)


for x in os.listdir():
    if x.endswith(".txt"):
        print(x)
        os.path.isdir


# goes into subdirectorys and prints what is in it
"""
res=[]
for (path, dir_names, file_names) in walk(path):
    res.extend(file_names)
    # don't look inside any subdirectory
    
print(res)
"""
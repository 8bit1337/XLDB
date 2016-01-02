#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#or you could use os.walk() which will yield two lists for each directory it visits - splitting into files and dirs for you. If you only want the top directory you can just break the first time it yields

#from os import walk

#f = []
#for (dirpath, dirnames, filenames) in walk(mypath):
 #   f.extend(filenames)
  #  break

from os import listdir
from os.path import isfile, join
currdir = 'C:/Users/Jason/Games/Atari800WinPLus/Games'
#currdir = 'C:/Users/jasong.MARTRON/Games/Atari800WinPLus/Games'
files = listdir(currdir)
i=0
print(files[0:3])
for f in files:
    if isfile(join(currdir, f)):
        print('File: ' + f)
    else:
        print('Dir : ' + f)
    
    i+=1
    if i == 3:
        break
    


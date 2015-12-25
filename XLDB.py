#from os import listdir
#from os.path import isfile, join


#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#or you could use os.walk() which will yield two lists for each directory it visits - splitting into files and dirs for you. If you only want the top directory you can just break the first time it yields

#from os import walk

#f = []
#for (dirpath, dirnames, filenames) in walk(mypath):
 #   f.extend(filenames)
  #  break

from os import listdir
#chdir('C:/Users/jasong.MARTRON/Games/Atari800WinPLus/Games')
files = listdir('C:/Users/jasong.MARTRON/Games/Atari800WinPLus/Games')
print(files[0])



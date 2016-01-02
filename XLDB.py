#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#or you could use os.walk() which will yield two lists for each directory it visits - splitting into files and dirs for you. If you only want the top directory you can just break the first time it yields

#from os import walk

#f = []
#for (dirpath, dirnames, filenames) in walk(mypath):
 #   f.extend(filenames)
  #  break

from os import listdir
from os.path import isfile, join, dirname
workdir = dirname(__file__)
ataridir = 'C:/Users/Jason/Games/Atari800WinPLus/Games'
#ataridir = 'C:/Users/jasong.MARTRON/Games/Atari800WinPLus/Games'

files = listdir(ataridir)
i=0

data = open(join(workdir, 'DataDump.csv'), 'w')


dirs = []
for f in files:
    currf = join(ataridir, f)
    if isfile(currf):
        file = open(currf, 'rb')
        first71 = str(file.read(71))
        
        towrite = '|'.join([f, first71])
        print(towrite)
        data.write(towrite)
    i+=1
    if i == 3:
        break

for di in dirs:
    print('Dir : ' + d)

file.close()
data.close()


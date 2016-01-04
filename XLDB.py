##### INITIALIZE #####
from os import listdir
from os.path import isfile, join, dirname
workdir = dirname(__file__)
ataridir = 'C:/Users/Jason/Games/Atari800WinPLus/Games'
#ataridir = 'C:/Users/jasong.MARTRON/Games/Atari800WinPLus/Games'

### FUNCTIONS ###
def processDir(files, directory, exportfile):
    dirs = []

    print('Processing: ' + directory)
    for f in files:
        currf = join(directory, f)
        if isfile(currf):
            file = open(currf, 'rb')
            first71 = str(file.read(71)).replace('|','').replace('\\','')

            towrite = '|'.join([f, first71]) + '\n'
               
            exportfile.write(towrite)
        else:
            dirs += [f]
        

    #now process sub directories
    for d in dirs:
        newdir = directory + '/' + d
        files = listdir(newdir)
        processDir(files, newdir, exportfile)

##### KERNAL ####
exportfile = open(join(workdir, 'DataDump.csv'), 'w')
files = listdir(ataridir)
processDir(files, ataridir, exportfile)


exportfile.close()



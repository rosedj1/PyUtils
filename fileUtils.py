import os
from shutil import copy2

##__________________________________________________________________||
### CAN PROBABLY JUST USE: from shutil import copyfile ... LOL
def copyFile(inDir,fileName,outDir):
    '''
    inDir       = source dir which contains fileName
    outDir      = destination dir to put fileName
    fileName    = file name
    '''
    ## Make directory if it doesn't exist
    makeDirs(outDir)
    ## Check if file already exists in outDir
    if not os.path.exists(outDir+fileName):
        copy2(inDir+fileName, outDir+fileName)

##______________________________________________
def makeDirs(dir):                       
    if not os.path.exists(dir):          
        os.makedirs(os.path.abspath(dir))

##__________________________________________________________________||
#def mkdir_p(path):
#    # http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
#    try:
#        os.makedirs(path)
#    except OSError as exc: # Python >2.5
#        if exc.errno == errno.EEXIST and os.path.isdir(path):
#            pass
#        else: raise

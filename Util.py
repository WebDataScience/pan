from shutil import copy
from sklearn.cross_validation import KFold
from CSVMaker import csvLineMaker
import os, csv

#Save textual content to a file
#Input: file path and textual content
def saveFile (path, content):
    file(path,"wb").writelines(content)

#Extract files from the folder
def getFilesFromFolder(folderPath):
    files = [f for f in os.listdir(folderPath) if f.endswith('.xml')]
    return files
#Read content of the file    
def readFile(filePath):
    text = open(filePath, 'r').read()
    return text

def saveFolder(folderPath):  
    if not os.path.exists(folderPath):
        os.makedirs(folderPath) 
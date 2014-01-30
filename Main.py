import os
from FeatureExtractor import extractDataFilesAndFeatures
from Util import saveFolder

def extractFolderPath(path):
    index = path.find('/')
    while index!=-1:
        lastIndex = index
        index = path.find('/', index+1)  
    folderPath = path[0:lastIndex+1]
    return folderPath

def doPreProcessingAndTraining(trainDB):
    model = ''
    path = extractFolderPath(trainDB)
    finalPath = path+'blogs_final'
    saveFolder(finalPath)
    resultPath =path+'blogs_result'
    saveFolder(resultPath)
    #read files from the train DB and extract features
    extractDataFilesAndFeatures(trainDB,finalPath,resultPath)
    #make a model
    return model
    
def doProcessingAndTesting(testDB):
    result =''
    #read files from the test DB
    #run the model on test data
    #get prediction file
    return result
    
def run(trainDB, testDB):
    doPreProcessingAndTraining(trainDB)
    doProcessingAndTesting(testDB)
    
doPreProcessingAndTraining('/Users/Golnoosh/Documents/Blog data/blogs')

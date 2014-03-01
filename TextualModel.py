from CosineCSVMaker import cosineCSVMaker
from LabelCollector import concatFiles
from CosineSimilarity import cosineMeasure
from TextualFeatureExtractor import extractTextualFeatures
from Util import extractFolderName, extractFileName
import os,csv
# extract all the textual features of all the files in the training directory:path is the training directory
#subject can be training or testing
def makeTextualModelDoctionary(path, labels, subject, type, lang):
    textualDictionary = {}
    files = [f for f in os.listdir(path) if f.endswith('.xml')]
    # extract features of each document
    for filePath in files:
        folderPath = extractFolderName(path)
        filePath = folderPath+filePath
        textFileName = extractFileName(filePath)
        print textFileName
        info = textFileName.split('_')
        fileName = textFileName.replace('xml','txt')
        cleanFilePath = getHomeDirectory()+type+'_'+lang+'/'+subject+'/clean'+fileName
        features = extractTextualFeatures(cleanFilePath, filePath,userID, lang)
        # add all the textual features of a file to the dictionary of textual features
        textualDictionary[userID] = features
    # extract features of each label
    for label in labels:
        cleanLablePath=getHomeDirectory()+type+'_'+lang+'/'+subject+'/grouped/'+label+'.txt'
        xmlLabelPath=getHomeDirectory()+type+'_'+lang+'/'+subject+'/grouped/'+'_xml.txt'
        features = extractTextualFeatures(cleanLablePath, xmlLabelPath, label ,lang)
        textualDictionary[label] = [features]
        
    return textualDictionary
                       
#extract userID from the file name      
def extractID(filePath):
    info = filePath.split('_')
    userID = str(info[0])
    return userID

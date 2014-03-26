from CosineCSVMaker import cosineCSVMaker
from LabelCollector import concatFiles
from CosineSimilarity import cosineMeasure
from TextualFeatureExtractor import extractTextualFeatures
from Util import extractFolderName, extractFileName,getHomeDirectory
from LIWC import getEnglishLiwcDic,getSpanishLiwcDic
import os,csv
# extract all the textual features of all the files in the training directory:path is the training directory
#subject can be training or testing
def makeTextualModelDoctionary(path, labels, subject, type, lang):
    if lang =='en':
        LIWCDic = getEnglishLiwcDic()
    elif lang =='es':
        LIWCDic = getSpanishLiwcDic()
    textualDictionary = {}
    files = [f for f in os.listdir(path) if f.endswith('.xml')]
    # extract features of each document
    for filePath in files:
        folderPath = extractFolderName(path)
        filePath = folderPath+filePath
        textFileName = extractFileName(filePath)
        print textFileName
        info = textFileName.split('_')
        userID = info[0]
        fileName = textFileName.replace('xml','txt')
        cleanFilePath = "/Users/the_james_marq/PAN-tests/text_stuff/"+type+'_'+lang+'/'+subject+'/clean/'+fileName
        features = extractTextualFeatures(cleanFilePath, filePath,userID, lang, LIWCDic)
        # add all the textual features of a file to the dictionary of textual features
        textualDictionary[userID] = features
    # extract features of each label
    for label in labels:
        cleanLablePath="/Users/the_james_marq/PAN-tests/text_stuff/"+type+'_'+lang+'/'+subject+'/grouped/'+label+'.txt'
        xmlLabelPath="/Users/the_james_marq/PAN-tests/text_stuff/"+type+'_'+lang+'/'+subject+'/grouped/'+label+'_xml.txt'
        features = extractTextualFeatures(cleanLablePath, xmlLabelPath, label ,lang, LIWCDic)
        textualDictionary[label] = features
        
    return textualDictionary
                       
#extract userID from the file name      
def extractID(filePath):
    info = filePath.split('_')
    userID = str(info[0])
    return userID

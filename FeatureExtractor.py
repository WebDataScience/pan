import os
from Util import saveFile,getFilesFromFolder,readFile
from CSVMaker import csvLineMaker

#Make the header for textual features
def getTextualHeaderFeatures():
    header = []
    header.append('numberOfPosts');
    header.append('averageNumberOfTokensPerPost');
    header.append('numberOfSmiley');
    header.append('numberOfIndividualToken');
    return header

#Make the header for temporal features
def getTemporalHeaderFeatures():
    header = []
    header.append('morningActivity');
    header.append('eveningActivity');
    header.append('nightActivity');
    header.append('midNightActivity');
    header.append('frequency');
    return header

#Make the header for class features
def getClassHeaderFeatures():
    header = []
    header.append('userId');
    header.append('age');
    header.append('gender');
    header.append('job');
    header.append('place');
    header.append('ageClass')
    return header

#################################################################################
#Extract the textual content and features of each users and combine them in one text file
#Input: file path
#Output: Textual content
def extractTextAndFeatures(filePath):
    content = readFile(filePath)
    posts, text = extractText(content)
    textualfeatures = extractTextualFeatures(text)
    temporalFeatures = extractTemporalFeatures(content)
    return text, textualfeatures, temporalFeatures

#Extract posts from the the XML files 
def extractText(content):
    texts= []
    startPost = content.find('<post>')
    allText = ''
    while startPost!=-1:
        post = ''
        endPost = content.find('</post>',startPost)
        post = content[startPost+len('<post>'): endPost]
        #remove additional start and end spaces of each post
        post = post.strip()
        content = content[endPost+1:]
        texts.append(post)
        allText = allText+post+'\n'
        startPost = content.find('<post>')
    return texts, allText


def extractTimes(content):
    times = []
    startTime = content.find('<date>')
    if startTime !=-1:
        postTime = ''
        endTime = content.find('</date>',)
        postTime = content[startTime: endTime]
        content = content[endTime+1:]
        times.append(postTime)
    return times

#Extract textual features from each user's blog posts
def extractTextualFeatures(text):
    features = []
    return features

    
#Extract temporal features from each user's blog posts
def extractTemporalFeatures(filePath):
    features = []
    return features

#Extract LIWC features   
def extractLIWCFeatures(textualFolderPath):
    text = ''
    features = []
    return text, features

def extractAgeClass(age):
    if age<20:
        ageClass = 'A'
    elif age<30:
        ageClass='B'
    elif age<40:
        ageClass='C'
    else:
        ageClass='D'
    return ageClass
        
#################################################################################
#Make a folder including textual content of each user
def extractDataFilesAndFeatures(initialFolderpath,finalFolderPath, resultFolderPath):
    csvTextualFeature = csvLineMaker(getTextualHeaderFeatures())+'\n'
    csvTemporalFeature = csvLineMaker(getTemporalHeaderFeatures())+'\n'
    csvClassFeature = csvLineMaker(getClassHeaderFeatures())+'\n'
    fileNames = getFilesFromFolder(initialFolderpath)
    for fileName in fileNames: 
        content, textFeatures, temporalFeatures = extractTextAndFeatures(initialFolderpath+'/'+fileName)
        info = fileName.split('.')
        userID = str(info[0])
        gender = str(info[1])
        age = str(info[2])
        ageClass = str(extractAgeClass(float(age)))
        job = str(info[3])
        place = str(info[4])
        saveFile(finalFolderPath+'/'+userID+'.txt', content)
        csvTextLine= csvLineMaker(textFeatures)
        classFeatures = []
        classFeatures.append(userID)
        classFeatures.append(age)
        classFeatures.append(gender)
        classFeatures.append(job)
        classFeatures.append(place)
        classFeatures.append(ageClass)
        csvClassLine = csvLineMaker(classFeatures)
        csvTemporalLine= csvLineMaker(temporalFeatures)
        csvClassFeature = csvClassFeature+csvClassLine+'\n'
        csvTextualFeature = csvTextualFeature+csvTextLine+'\n'
        csvTemporalFeature = csvTemporalFeature+csvTemporalLine+'\n'
    saveFile(resultFolderPath+'/textualFeature.csv', csvTextualFeature)  
    saveFile(resultFolderPath+'/temporalFeature.csv', csvTemporalFeature)
    saveFile(resultFolderPath+'/classFeature.csv', csvClassFeature)

    
    

# extract all the textual features of all the files in the training directory:path is the training directory
#labels = ["18-24_male", "18-24_female", "25-34_male", "25-34_female", "35-49_male", "35-49_female", "50-64_male", "50-64_female", "65-xx_male", "65-xx_female"]
def makeTextualModelDoctionary(path, labels):
    textualDictionary = dic()
    files = listAllFiles(path)
    # extract features of each document
    for filePath in files:
        if filePath.find('.xml'):
            userID = extractID(filePath)
            features = extractTextualFeatures(filePath)
            # add all the textual features of a file to the dictionary of textual features
            textualDictionary[userID] = features
    # extract features of each label
    for label in labels:
        labelPath = "../Data/grouped/"+label+"/result.txt"
        features = extractTextualFeatures(labelPath)
        textualDictionary[label] = features
    return textualDictionary
    
                   
#extract userID from the file name      
def extractID(filePath):
    info = filePath.split('_')
    userID = str(info[0])
    return userID
    
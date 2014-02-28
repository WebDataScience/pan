from Util import saveFile
from CSVMaker import csvLineMaker

# input : list of users and lables, 
# textual dictionary from textualmodel.py
#output path to write the csv file
def cosineCSVMaker(users, lables, textFeatureDictionary, outputPath):
    csvContent = ''
    for user in users:
        scores = []
        #if we want the userID to be in the output file
        scores.append(user)
        for label in labels:
            scores.append(cosineMeasure([textFeatureDictionary[user]], [textFeatureDictionary[label]]))
        row = csvLineMaker(scores)
        csvContent = csvContent+row+'\n'
    saveFile(csvContent,outputPath+'/textualFeatures.csv')
         
    
    
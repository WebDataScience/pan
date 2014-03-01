from Util import saveFile
from CSVMaker import csvLineMaker
from CosineSimilarity import cosineMeasure
import os,csv

# input : list of users and lables, 
# textual dictionary from textualmodel.py
#output path to write the csv file
def cosineCSVMaker(users, labels, textFeatureDictionary):
    cosineScoreDic= {}
    for user in users:
        scores = []
        for label in labels:
            scores.append(cosineMeasure(textFeatureDictionary[user], textFeatureDictionary[label]))
        cosineScoreDic[user]= scores
    return cosineScoreDic
         
    
    
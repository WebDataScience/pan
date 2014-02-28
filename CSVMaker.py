import os

#CSV element separator       
def getCsvSeparator():
    return ','

#Make one element in double quotation
def makeCsvElement(element):
    return '"'+element+'"'

#Get a feature set and make a CSV line
def csvLineMaker(features):
    csvLine = ''
    for feature in features:
        csvLine = csvLine+ makeCsvElement(feature)+ getCsvSeparator()
    return csvLine


def dictionaryToCsv(myDict, filePath):
    writer = csv.writer(open(filePath, 'wb'))
    for key, value in myDict.items():
        writer.writerow([key, value])
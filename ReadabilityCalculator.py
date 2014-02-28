from nltk.corpus import cmudict
from curses.ascii import isdigit
import re

def textAnalyzer(text, tokens):
    analyzedVars = {}
    analyzedVars['words'] = tokens
    analyzedVars['charCount'] = float(CharCount(tokens))
    wordCount= float(len(tokens))
    analyzedVars['wordCount'] = float(len(tokens))
    sentenceCount=SentenceCount(text)
    analyzedVars['sentenceCount'] = float(SentenceCount(text))
    #analyzedVars['syllableCount'] = float(SyllableCalculator(text))
    #analyzedVars['complexwordCount'] = float(complexwordsCount)
    averageWordsPerSentence = float(float(wordCount)/float(sentenceCount))
    analyzedVars['averageWordsPerSentence'] = float(averageWordsPerSentence)
    return analyzedVars
  
def SyllableCalculator(text):
    d = cmudict.dict()
    counter = 0.0
    tokens = re.findall("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+",text)
    for token in tokens:
        count = 1.0
        if token.lower() in d.keys():
            count =max([len(list(y for y in x if isdigit(y[-1]))) for x in d[token.lower()]])
        counter = counter+count
    return counter

def SentenceCount(text):
    matches = re.findall('[^.!?]+[.!?]',text)
    return len(matches)

    
def CharCount(tokens):
    count = 0.0
    for token in tokens:
        count= count+ len(token)
    return float(count)
            
def GunningFogIndex(text,analyzedVars):
    score = 0.4 * ((analyzedVars['averageWordsPerSentence']) + (100 * (analyzedVars['complexwordCount']/analyzedVars['wordCount'])))
    return round(score, 4)

def ARI(text,analyzedVars):
    score = 4.71 * (analyzedVars['charCount'] / analyzedVars['wordCount']) + 0.5 * (analyzedVars['wordCount'] / analyzedVars['sentenceCount']) - 21.43
    return score

def FleschReadingEase(text,analyzedVars):
    score = 0.0
    score = 206.835 - (1.015 * (analyzedVars['averageWordsPerSentence'])) - (84.6 * (analyzedVars['syllableCount']/ analyzedVars['wordCount']))
    return round(score, 4)


def FleschKincaidGradeLevel(text,analyzedVars):
    score = 0.39 * (analyzedVars['averageWordsPerSentence']) + 11.8 * (analyzedVars['syllableCount']/ analyzedVars['wordCount']) - 15.59
    return round(score, 4)

def SMOGIndex(text, analyzedVars):
    score = (math.sqrt(analyzedVars['complexwordCount']*(30/analyzedVars['sentenceCount'])) + 3)
    return score

def ColemanLiauIndex(text, analyzedVars):
    score = (5.89*(analyzedVars['charCount']/analyzedVars['wordCount']))-(30*(analyzedVars['sentenceCount']/analyzedVars['wordCount']))-15.8
    return round(score, 4)

def RIX(text, analyzedVars):
    score = 0.0
    longwords = 0.0
    for word in analyzedVars['words']:
        if len(word) >= 7:
            longwords += 1.0
    score = longwords / analyzedVars['sentenceCount']
    return score

def extractReadabilityArray(text, tokens):
    readArray = []
    analyzedVars = textAnalyzer(text, tokens)
    readArray.append(analyzedVars['charCount'])
    readArray.append(analyzedVars['sentenceCount'])
    #readArray.append(analyzedVars['syllableCount'])    
    readArray.append(analyzedVars['averageWordsPerSentence'])                                 
    readArray.append(float(ARI(text,analyzedVars)))
    readArray.append(float(RIX(text,analyzedVars)))
    readArray.append(float(ColemanLiauIndex(text,analyzedVars)))
    #readArray.append(SMOGIndex(text,analyzedVars))
    #readArray.append(float(FleschKincaidGradeLevel(text,analyzedVars)))
    #readArray.append(float(FleschReadingEase(text,analyzedVars)))
    #readArray.append(GunningFogIndex(text,analyzedVars))
    #print readArray
    return readArray
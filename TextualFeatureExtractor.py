from nltk.corpus import wordnet 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag.stanford import POSTagger
from nltk.corpus import cmudict
from os import listdir
from os.path import isfile, join
#from bs4 import BeautifulSoup
from Util import extractFileName, readFile
from ReadabilityCalculator import extractReadabilityArray
import re

# text path as an input 
def extractTextualFeatures(textFilePath, xmlFilePath):
    #call all the feature extractor and make a vector out of them
    features = []
    textFileName =extractFileName(xmlFilePath)
    print textFileName
    info = textFileName.split('_')
    userID = str(info[0])
    print userID
    lang = str(info[1])
    text = readFile(textFilePath)
    xmlText= readFile(xmlFilePath)
    documentCounter = extractNumberOfDocument(xmlText)
    features.append(documentCounter)
    tokens = extractTokens(text)
    length = len(tokens)
    print length
    features.append(length)
    tokens = removeStopWords(text, lang)
    formality = extractFormality(tokens, lang)
    print formality
    features.append(formality)
    repeatation = extractRepeatation(tokens, text)
    print repeatation
    features.append(repeatation)
    capitalWord, capitalLetter = ExtractCapital(tokens)
    print capitalWord
    print capitalLetter
    features.append(capitalWord)
    features.append(capitalLetter)
    emoticon = extractEmoticons(text, tokens)
    print emoticon
    features.append(emoticon)
    errorArray = extractErrors(text)
    features.extend(errorArray)
    #posArray = extractPOSFeatures(text, lang)
    #features.append(posArray)
    htmlArray = extractHTMLTags(xmlText,tokens)
    print htmlArray
    features.extend(htmlArray)
    readabilityFeatures = extractReadability(text)
    features.extend(htmlArray)
    return features

def extractNumberOfDocument(text):
    number = countMatch('</document>',text)
    return number

#Count number of words which are in the WordNet dictionary
def extractFormality(tokens, lang):
    number = 0
    for token in tokens:
        if lang =='en':
            if wordnet.synsets(token):
                number = number + 1
        else:
            #TODO: look for spanish dictionary
            number = 0
    return float(float(number)/float(len(tokens)))

#Extract tokens using nltk tool
def extractTokens(text):
    tokens = word_tokenize(text)
    return tokens

#Extract number of tokens which are repeated during posts
def extractRepeatation(tokens, text):
    number = 0
    for word in tokens:
        number = getAllTheMatch(word, text)
    frequencyOfRepeatation = float(float(number)/float(len(tokens)))
    return frequencyOfRepeatation

#Return the text which after finding one match, if it in none and zero, there is no match, otherwise there is a match and remaining text is returned
def countMatch(search, text):
    index = text.find(search)
    if index ==-1:
        return None,0
    else:
        end = index+len(search)
        text = text[end:]
        return text,1
    
#Count number of matches of a token in whole text content 
def getAllTheMatch(search, text):
    count = 0
    while True:
        text, number = countMatch(search, text)
        if number==1:
            count = count+1
        else:
            break
    return count
    
#Extract capital letters and words
def ExtractCapital(tokens):
    capitalLetter = 0
    capitalWord = 0
    wholeSize = 0
    for token in tokens:
        size = len(token)
        wholeSize= wholeSize+size
        uppers = [l for l in token if l.isupper()]
        length = len(uppers)
        capitalLetter = capitalLetter+length
        if size == length:
            capitalWord = capitalWord+1
    return float(float(capitalWord)/float(len(tokens))), float(float(capitalLetter)/float(wholeSize))

#Remove stop words from the text
# This function is language dependent, therefore it is needed to detect the language first and then run this function on that particular langiage
# this function is for English
def removeStopWords(text, lang):
    tokens = extractTokens(text)
    if lang =='en':
        filteredToken = [w for w in tokens if not w in stopwords.words('english')]
    elif lang =='es':
        filteredToken = [w for w in tokens if not w in stopwords.words('spanish')]
    return filteredToken

# Extract number of simple emoticons per document 
def extractEmoticons(text, tokens):
    matches = re.findall(r'(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    return float(float(len(matches))/float(len(tokens)))
            
            
def extractErrors(text):
    #TODO: add gayathri's work to extract errors here
    errorArray = []
    grammerError = spellingError =0
    errorArray.append(grammerError)
    errorArray.append(spellingError)
    return errorArray
    
    
def extractPOSFeatures(text, tokens, lang):
    print text
    if lang == 'en':
        st = POSTagger('./stanford-postagger-full-2014-01-04/models/english-bidirectional-distsim.tagger','stanford-postagger-full-2014-01-04/stanford-postagger.jar')
    elif lang =='es':
        #TODO: add spanish POS taggers
        st = POSTagger('./stanford-postagger-full-2014-01-04/models/english-bidirectional-distsim.tagger','stanford-postagger-full-2014-01-04/stanford-postagger.jar')
    ret = st.tag(tokens)
    for tag in ret:
        if tag[1] in doc_arr:
            doc_arr[tag[1]]+=1
        else:
            doc_arr[tag[1]]=1
    return doc_arr


def extractHTMLTags(text, tokens):
    docArray = []
    docArray.append(float(float(getAllTheMatch('<a',text))/float(len(tokens))))
    docArray.append(float(float(getAllTheMatch('<img',text))/float(len(tokens))))
    docArray.append(float(float(getAllTheMatch('<b',text))/float(len(tokens))))
    docArray.append(float(float(getAllTheMatch('<i',text))/float(len(tokens))))
    docArray.append(float(float(getAllTheMatch('<ui',text) + getAllTheMatch('<ol',text))/float(len(tokens))))
    return docArray   

# extract different features related to readability of the text based on the different formulas
def extractReadabilityFeatures(text,tokens):
    readabilityArray = extractReadabilityArray(text,tokens)
    # this works for english 
    return readabilityArray
    
   
#print extractTextualFeatures('/Users/Golnoosh/Documents/Blog-data/Data-2014/pan14-author-profiling-training-corpus-2014-02-10/pan14-author-profiling-training-corpus-blogs-2014-02-10/en/4c9fe29d6bea6d70c02b7eca7e2fac7b_en_50-64_male.xml')
    
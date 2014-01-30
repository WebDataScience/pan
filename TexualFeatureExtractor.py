from nltk.corpus import wordnet 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#Count number of words which are in the WordNet dictionary
def extractFormality(tokens):
    number = 0
    for token in tokens:
        if wordnet.synsets(token):
            number = number + 1
    number = float(float(number)/float(len(tokens)))
    return number

#Extract tokens using nltk tool
def extractTokens(text):
    tokens = word_tokenize(text)
    return tokens

#Extract number of tokens which are repeated during posts
def extractRepeatation(tokens, text):
    number = 0
    for word in tokens:
        number = getAllTheMatch(word, text)
    frequencyOfRepeatation = number/len(tokens)
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
    for token in tokens:
        size = len(token)
        uppers = [l for l in token if l.isupper()]
        length = len(uppers)
        capitalLetter = capitalLetter+length
        if size == length:
            capitalWord = capitalWord+1
    return capitalWord, capitalLetter

#Remove stop words from the text
# This function is language dependent, therefore it is needed to detect the language first and then run this function on that particular langiage
# this function is for English
def removeStopWords(text):
    tokens = extractTokens(text)
    filteredToken = [w for w in tokens if not w in stopwords.words('english')]
    return filteredToken




    
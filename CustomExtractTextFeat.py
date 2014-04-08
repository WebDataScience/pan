import os, argparse
from Util import readFile,saveFile,extractFileName,clean,getHomeDirectory,saveDictionary,saveStringDictionary, saveDictionaryValues
from TextualModel import makeTextualModelDoctionary
from CosineCSVMaker import cosineCSVMaker
from shutil import rmtree

folder = '/Users/the_james_marq/PAN-tests/twitter-en/Cleaned'
labels = ['18-24 male','18-24 female', '25-34 male', '25-34 female', '35-49 male', '35-49 female','50-64 male','50-64 female','60-xx male','60-xx female']
subject = 'twitter'
type = 'training'
lang = 'en'
output = '/Users/the_james_marq/PAN-tests/text_stuff/twitter_en/training'

textualDic = makeTextualModelDoctionary(folder, labels, subject, type, lang)
saveDictionary(textualDic,output +'dictionary/textual+ID.csv')
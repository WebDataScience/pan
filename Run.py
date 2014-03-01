import os
from Util import readFile,saveFile,extractFileName,clean,getHomeDirectory,saveDictionary,saveDictionaryValues
from TextualModel import makeTextualModelDoctionary
from CosineCSVMaker import cosineCSVMaker
from shutil import rmtree



def run(input_training, input_testing, type, lang, output_results):
    print "Starting.."
    if os.path.exists(getHomeDirectory()+type+'_'+lang+'/'):
        rmtree(getHomeDirectory() +type+'_'+lang+'/')
    os.makedirs(getHomeDirectory() +type+'_'+lang+'/')
    output = getHomeDirectory() +type+'_'+lang+'/'
    if os.path.exists(output +'training/'):
        rmtree(output +'training/')
    os.makedirs(output +'training/')
    if os.path.exists(output +'testing/'):
        rmtree(output +'testing/')
    os.makedirs(output +'testing/')
    if os.path.exists(output +'testing/'+'dictionary/'):
        rmtree(output +'testing/'+'dictionary/')
    os.makedirs(output +'testing/'+'dictionary/')
    if os.path.exists(output +'training/'+'dictionary/'):
        rmtree(output +'training/'+'dictionary/')
    os.makedirs(output +'training/'+'dictionary/')
    
    print "Pre-process the TRAINING data"
    folder = input_training
    outputfolder = getHomeDirectory() +type+'_'+lang+'/training/'
    extractingCSVModel(folder, outputfolder, 'training',type,lang)
    print "Pre-process the TESTING data"
    folders = input_testing
    outputfolder = getHomeDirectory() +type+'_'+lang+'/testing/'
    extractingCSVModel(folder,outputfolder,'testing',type,lang)
  
    
def extractingCSVModel(folder, output,subject,type,lang):
    print "Pre-processing step started..."
    users, labels, cleanPath, groupPath = preProcessing(folder, output)
    print "Pre-processing step finished..."
    print "Extracting features..."     
    print "Extracting LDA features..."  
    #LDADic = extractTopicFeatures(folder)
    #KldivDic = klDive(LDADic)
    print "LDA features are ready!"
    print "Extracting Textual features..."
    textualDic = makeTextualModelDoctionary(folder, labels, subject, type, lang)
    saveDictionary(textualDic,output +'dictionary/textual+ID.csv')
    saveDictionaryValues(textualDic,output +'dictionary/textual-ID.csv')
    cosineDic = cosineCSVMaker(users, labels, textualDic)
    saveDictionary(cosineDic,output +'dictionary/cosine+ID.csv')
    saveDictionaryValues(cosineDic,output +'dictionary/cosine-ID.csv')
    print "Textual features are ready!"    
    print "Combining the feature sets.."
    #combinedDistanceDic = combineFeatures(topicDic, textualDic, users)    
    #saveDictionary(combinedDistanceDic,output +'dictionary/combinedDistance+ID.csv')
    #saveDictionaryValues(combinedDistanceDic,output +'dictionary/combinedDistance-ID.csv')
    #combinedFeaturesDic = combineFeatures(KldivDic, cosineDic, users)  
    #saveDictionary(combinedFeaturesDic,output +'dictionary/combinedFeatures+ID.csv')
    #saveDictionaryValues(combinedFeaturesDic,output +'dictionary/combinedFeatures-ID.csv')
    print "CSV model is ready"   
            
def preProcessing(folderPath, outputPath):
    print "Make the clean data set"
    cleanPath = outputPath+ '/Clean'
    if not os.path.exists(cleanPath):
        os.makedirs(cleanPath)  
    print "Make the grouped files"
    groupedPath = outputPath+ '/grouped'
    if not os.path.exists(groupedPath):
        os.makedirs(groupedPath) 
    users , labels= cleanText(folderPath, cleanPath, groupedPath)  
    return users, labels, cleanPath, groupedPath
    
def cleanText(folder, textualOutput, groupedPath):
     files = [f for f in os.listdir(folder) if f.endswith('.xml')]
     labels = []
     users = []
     labelDict = {}
     count = 0
     for file in files:
         count = count+1
         print count
         xmlText = readFile(folder+file)
         text = clean(xmlText)
         info = file.split('_')
         userID = info[0]
         age = info[2]
         gender = info[3].replace('.xml','')   
         label = age+'_'+gender
         users.append(userID)
         if label in labelDict.keys():
             text_label = labelDict[label]
             text_label = text_label +text
             labelDict[label]=text_label
             xml_label = labelDict[label+'_xml']
             xml_label = xml_label +xmlText
             labelDict[label+'_xml']=xml_label
         else:
             labelDict[label] = text
             labelDict[label+'_xml'] = xmlText
         if label not in labels:
             labels.append(label)
         fileName = file.replace('.xml','.txt')
         textualFile = textualOutput+'/'+ fileName
         saveFile(textualFile,text)
     for label in labels:
         groupedFile = groupedPath+'/'+label+'.txt'
         groupedXmlFile = groupedPath+'/'+label+'_xml'+'.txt'
         saveFile(groupedFile, labelDict[label])
         saveFile(groupedXmlFile,labelDict[label+'_xml'])
     return users, labels
         

input_training='/Users/Golnoosh/Documents/Blog-data/Data-2014/pan14-author-profiling-training-corpus-2014-02-10/pan14-author-profiling-training-corpus-blogs-2014-02-10/en/'
input_testing= '/Users/Golnoosh/Documents/Blog-data/Data-2014/pan14-author-profiling-training-corpus-2014-02-10/pan14-author-profiling-training-corpus-blogs-2014-02-10/en/'
type ='blog'
lang = 'en'
output_results=''
run(input_training, input_testing, type, lang, output_results)
    
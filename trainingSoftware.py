import os, argparse
from Util import readFile,saveFile,extractFileName,clean,getHomeDirectory,saveDictionary,saveStringDictionary, saveDictionaryValues
from TextualModel import makeTextualModelDoctionary
from CosineCSVMaker import cosineCSVMaker
from TopicModeling import extractTopicFeatures
from shutil import rmtree


def run(input_training, type, lang, output_results):
    print "Starting.."
    homedir = "./Data/"
    if os.path.exists(homedir+type+'_'+lang+'/'):
        rmtree(homedir +type+'_'+lang+'/')
    os.makedirs(homedir +type+'_'+lang+'/')
    output = homedir +type+'_'+lang+'/'
    if os.path.exists(output +'training/'):
        rmtree(output +'training/')
    os.makedirs(output +'training/')
    if os.path.exists(output +'training/'+'dictionary/'):
        rmtree(output +'training/'+'dictionary/')
    os.makedirs(output +'training/'+'dictionary/')
    
    print "Pre-process the TRAINING data"
    folder = input_training
    outputfolder = homedir +type+'_'+lang+'/training/'
    extractingCSVModel(folder, outputfolder, 'training',type,lang)
    
def extractingCSVModel(folder, output,subject,type,lang):
    print "Pre-processing step started..."
    users, labels, cleanPath, groupPath, classDict = preProcessing(folder, output)
    print "Pre-processing step finished..."
    saveStringDictionary(classDict,output +'dictionary/class+ID.csv')
    print "Extracting features..."     
    print "Extracting LDA features..."  
    #LDADic = extractTopicFeatures(folder)
    #KldivDic = klDiv(LDADic)
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
    users , labels, classDict= cleanText(folderPath, cleanPath, groupedPath)  
    return users, labels, cleanPath, groupedPath, classDict
    
def cleanText(folder, textualOutput, groupedPath):
     files = [f for f in os.listdir(folder) if f.endswith('.xml')]
     labels = []
     users = []
     labelDict = {}
     classhDict={}
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
         classhDict[userID] = label
         users.append(userID)
         if label in labelDict.keys():
             text_label = labelDict[label]
             text_label = text_label +text
             labelDict[label]=text_label
             xml_label = labelDict[label+'_xml']
             xml_label = xml_label +xmlText
             labelDict[label+'_xml']=xml_label
             if age in labelDict.keys():
                 text_age = labelDict[age]
                 text_age = text_age +text
                 labelDict[age]=text_age
                 xml_age = labelDict[age+'_xml']
                 xml_age = xml_age +xmlText
                 labelDict[age+'_xml']=xml_label
             else:
                 labelDict[age] = text
                 labelDict[age+'_xml'] = xmlText
             if gender in labelDict.keys():
                 text_gender = labelDict[gender]
                 text_gender = text_gender +text
                 labelDict[gender]=text_gender
                 xml_gender = labelDict[gender+'_xml']
                 xml_gender = xml_gender +xmlText
                 labelDict[gender+'_xml']=xml_gender
             else:
                 labelDict[gender] = text
                 labelDict[gender+'_xml'] = xmlText 
             
         else:
             labelDict[label] = text
             labelDict[label+'_xml'] = xmlText
         if label not in labels:
             labels.append(label)
         if age not in labels:
             labels.append(age)
         if gender not in labels:
             labels.append(gender)
         fileName = file.replace('.xml','.txt')
         textualFile = textualOutput+'/'+ fileName
         saveFile(textualFile,text)
     for label in labels:
         groupedFile = groupedPath+'/'+label+'.txt'
         groupedXmlFile = groupedPath+'/'+label+'_xml'+'.txt'
         saveFile(groupedFile, labelDict[label])
         saveFile(groupedXmlFile,labelDict[label+'_xml'])
     return users, labels,classhDict

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Trains a model')
    parser.add_argument('-i','--input',help='Path to training corpus',required=True)
    parser.add_argument('-o','--output',help='Path to output directory',required=True)
    parser.add_argument('-l','--language',help='Language of training corpus',required=True)
    parser.add_argument('-g','--mediatype',help='Media type of training corpus',required=True)
    args = parser.parse_args()

    run(args.input, args.mediatype, args.language, args.output)
'''         
input_training='/Users/the_james_marq/PAN-tests/PAN14/blogs/en/'
input_testing= '/Users/the_james_marq/PAN-tests/PAN14/blogs/en/'
type ='blog'
lang = 'en'
output_results=''
run(input_training, input_testing, type, lang, output_results)

input_training='/Users/the_james_marq/PAN-tests/PAN14/blogs/es/'
input_testing= '/Users/the_james_marq/PAN-tests/PAN14/blogs/es/'
type ='blog'
lang = 'es'
output_results=''
run(input_training, input_testing, type, lang, output_results)

input_training='/Users/the_james_marq/PAN-tests/PAN14/reviews/en/'
input_testing= '/Users/the_james_marq/PAN-tests/PAN14/reviews/en/'
type ='reviews'
lang = 'en'
output_results=''
run(input_training, input_testing, type, lang, output_results)

input_training='/Users/the_james_marq/PAN-tests/PAN14/socialmedia/es/'
input_testing= '/Users/the_james_marq/PAN-tests/PAN14/sovialmedia/es/'
type ='socialmedia'
lang = 'es'
output_results=''
run(input_training, input_testing, type, lang, output_results)

input_training='/Users/the_james_marq/PAN-tests/PAN14/socialmedia/en/'
input_testing= '/Users/the_james_marq/PAN-tests/PAN14/socialmedia/en/'
type ='socialmedia'
lang = 'en'
output_results=''
run(input_training, input_testing, type, lang, output_results)

input_training='/Users/the_james_marq/PAN-tests/PAN14/twitter/es/'
input_testing= '/Users/the_james_marq/PAN-tests/PAN14/twitter/es/'
type ='twitter'
lang = 'es'
output_results=''
run(input_training, input_testing, type, lang, output_results)

input_training='/Users/the_james_marq/PAN-tests/PAN14/socialmedia/en/'
input_testing= '/Users/the_james_marq/PAN-tests/PAN14/socialmedia/en/'
type ='twitter'
lang = 'en'
output_results=''
run(input_training, input_testing, type, lang, output_results) 
'''   
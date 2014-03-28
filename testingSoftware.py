import os, argparse
from Util import readFile,saveFile,extractFileName,clean,getHomeDirectory,saveDictionary,saveStringDictionary, saveDictionaryValues
from TextualModel import makeTextualModelDoctionary
from CosineCSVMaker import cosineCSVMaker
from TopicModeling import extractTopicFeatures, klDivTesting
from shutil import rmtree
from libsvm.svm import *
from libsvm.svmutil import *

def run(input_testing, type, lang, output_results,model,output):
    print "Starting.."
    homedir = "./Data/"
    if os.path.exists(homedir+type+'_'+lang+'/'):
        rmtree(homedir +type+'_'+lang+'/')
    os.makedirs(homedir +type+'_'+lang+'/')
    output = homedir +type+'_'+lang+'/'
    if os.path.exists(output +'testing/'):
        rmtree(output +'testing/')
    os.makedirs(output +'testing/')
    if os.path.exists(output +'testing/'+'dictionary/'):
        rmtree(output +'testing/'+'dictionary/')
    os.makedirs(output +'testing/'+'dictionary/')
    
    print "Pre-process the testing data"
    folder = input_testing
    outputfolder = homedir +type+'_'+lang+'/testing/'
    extractingCSVModel(folder, outputfolder, 'testing',type,lang,model_name)
    
def extractingCSVModel(folder, output,subject,type,lang,model):
    topic_num = 100
    print "Pre-processing step started..."
    users, labels, cleanPath, groupPath, classDict = preProcessing(folder, output)
    print "Pre-processing step finished..."
    saveStringDictionary(classDict,output +'dictionary/class+ID.csv')
    print "Extracting features..."     
    print "Extracting LDA features..."  
    LDADic = extractTopicFeaturesTesting(cleanPath, topic_num, lang, type)
    KldivDic = klDivTesting(LDADic, groupPath,labels,topic_num,lang+"_"+type)
    print "LDA features are ready!"
    print "Extracting Textual features..."
    textualDic = makeTextualModelDoctionary(folder, labels, subject, type, lang)
    saveDictionary(textualDic,output +'dictionary/textual+ID.csv')
    saveDictionaryValues(textualDic,output +'dictionary/textual-ID.csv')
    #cosineDic = cosineCSVMaker(users, labels, textualDic)
    #saveDictionary(cosineDic,output +'dictionary/cosine+ID.csv')
    #saveDictionaryValues(cosineDic,output +'dictionary/cosine-ID.csv')
    print "Textual features are ready!"    
    print "Combining the feature sets.."
    combinedDistanceDic = combineFeatures(KldivDic, textualDic, classDict)    
    saveDictionary(combinedDistanceDic,output +'dictionary/combinedDistance+ID.csv')
    saveDictionaryValues(combinedDistanceDic,output +'dictionary/combinedDistance-ID.csv')
    #combinedFeaturesDic = combineFeatures(KldivDic, cosineDic, users)  
    #saveDictionary(combinedFeaturesDic,output +'dictionary/combinedFeatures+ID.csv')
    #saveDictionaryValues(combinedFeaturesDic,output +'dictionary/combinedFeatures-ID.csv')
    model = svm_load_model(model_name)
    for keys, values in combinedDistanceDic.iteritems():
    	print model.predict(values)
   
def combineFeatures(KLDivDic, textualDic, classDic):
    ret_dic = {}

    for keys, values in KLDivDic.iteritems():
        val = classDic[keys]
        val.append(values)
        val.append(textualDic[keys])
        ret_dic[keys] = val

    return ret_dic

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
    parser.add_argument('-i','--input',help='Path to testing corpus',required=True)
    parser.add_argument('-o','--output',help='Path to output directory',required=True)
    parser.add_argument('-l','--language',help='Language of testing corpus',required=True)
    parser.add_argument('-g','--mediatype',help='Media type of testing corpus',required=True)
    parser.add_argument('-m','--model',help='Location of model',required=True)
    args = parser.parse_args()

    run(args.input, args.mediatype, args.language, '',args.model, args.output)
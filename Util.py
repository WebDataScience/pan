import os, csv
import numpy as np
import os,csv

def getHomeDirectory():
    #return '/home/marquardt14/'
    return '/Users/Golnoosh/Documents/Blog-data/Data-2014/pan14-author-profiling-training-corpus-2014-02-10/output/'


def initDict(src):
	ret_dict = dict()
	onlyfiles = [ f for f in os.listdir(src) if os.path.isfile(os.path.join(src,f)) ]
	for entry in onlyfiles:
		file_info = entry.split("_")
		ret_dict[file_info[0]] = (file_info[2]+"_"+file_info[3].split(".")[0],[])
	return ret_dict

#Convert output of file inference to usable form
def fixMalletOutputInf(topicOutputPath, newPath, topic_num):
	print topicOutputPath
	print newPath
	#Convert .txt to appropriate .csv
	in_txt = csv.reader(open(topicOutputPath, "rb"), delimiter = '\t')
	output = csv.writer(open(newPath, 'wb'))

	next(in_txt, None)
	arr = [0] * (topic_num)
	for row in in_txt:	
		column_src = 0
		column_dst = 0
		index = 0
		topic_count = 0
		for word in row:
			entries = word.split(" ")
			for entry in entries:
				index += 1
				if index <= 2:
					continue

				if column_src%2 == 0:
					column_dst = entry
				else:
					arr[int(column_dst)]=entry
					topic_count+=1
				column_src+=1
				if topic_count >= topic_num:
					break
			output.writerow(arr)
	#if topicOutputPath != newPath:
	#	os.remove(topicOutputPath)

#Tranforms Mallet topic distribution output to normal row/column form
def fixMalletOutput(topicOutputPath, newPath, topic_num):
	in_txt = csv.reader(open(topicOutputPath, "rb"), delimiter = '\t')
	output = csv.writer(open(newPath, 'wb'))

	next(in_txt, None)
	for row in in_txt:
		arr = [0] * (topic_num + 1)
		column_src = 0
		column_dst = 0

		file_info = row[1].split("/")[-1]
		arr[0] = file_info.split("_")[0]

		for word in row[2:]:
			if column_src%2 == 0:
				column_dst = word
			else:
				arr[int(column_dst)+1] = word
			
			column_src+=1	
		
		output.writerow(arr)

#Save textual content to a file
#Input: file path and textual content
def saveFile (path, content):
    file(path,"wb").writelines(content)

#Extract files from the folder
def getFilesFromFolder(folderPath):
    files = [f for f in os.listdir(folderPath) if f.endswith('.xml')]
    return files
#Read content of the file    
def readFile(filePath):
    text = open(filePath, 'r').read()
    return text

def saveFolder(folderPath):  
    if not os.path.exists(folderPath):
        os.makedirs(folderPath) 

def readLines(fileName):        
    items = []
    if os.path.exists(fileName):
        f = open(fileName)
        lines = f.readlines()
        f.close()
        for line in lines:
            item = line.replace('\n', '')
            items.append(item)
        return items
    else:
        return None
       
def extractFileName(filePath):
	index = '/'
	temp =0
	slash = 0
	while slash<>-1:
		slash = filePath.find(index, temp)
		if slash<>-1:
			temp = slash+1
	fileName = filePath[temp:]
	return fileName


def extractFolderName(filePath):
	index = '/'
	temp =0
	slash = 0
	while slash<>-1:
		slash = filePath.find(index, temp)
		if slash<>-1:
			temp = slash+1
	fileName = filePath[:temp]
	return fileName
#initDict("/home/jamarq/PAN/Data/cleaned")

def clean(text):
    start_index = '<'
    finish_index = '>'
    text = text.replace('&lt;','<')
    text = text.replace('&gt;','>')
    starter = text.find(start_index)
    while starter<>-1:
        data_index = text.find('![CDATA[')
        if data_index<>-1:
            text = text.replace('<![CDATA[', '')
            text = text.replace(']]>', '')
            starter = text.find(start_index)
        else:
            finisher = text.find(finish_index,starter+1)
            if  finisher<>-1:
                rm_text = text[starter:finisher+1]
                text = text.replace(rm_text,' ')
                starter = text.find(start_index)
            else:
                starter =-1
    text = text.replace(']]>','')
    text = text.replace('\n',' ')
    text = text.strip() 
    
    text=cleanSpams(text) 
    text = cleanHtmlTags(text) 
    return text
        
def cleanHtmlTags(text):
    #print 'html'
    start = text.find('&')
    finish = start+20
    while  start <>-1 and (finish-start)<10:
        finish = text.find(';', start+1)
        if finish<>-1:
            rm = text[start:finish+1]
            text = text.replace(rm,' ')
        start = text.find('&')   
    return text
   
def cleanSpams(text):
    #print 'spam'
    start = text.find('%')
    while start <>-1:
		finish= text.find('%', start+1)
		index = start
		while finish<>-1 and float(finish-index) <5.0:
			index = finish
			finish = text.find('%', index+1)
		rm = text[start:index+1]
		text = text.replace(rm,' ')
		start = text.find('%')
    return text
   
def saveDictionary(myDic, filePath):
	writer = csv.writer(open(filePath, 'wb'))
	for key, value in myDic.items():
		writer.writerow([key]+ value)
        
def saveDictionaryValues(myDic, filePath):
    writer = csv.writer(open(filePath, 'wb'))
    for key, value in myDic.items():
        writer.writerow(value)
        
def saveStringDictionary(myDic, filePath):
    writer = csv.writer(open(filePath, 'wb'))
    for key, value in myDic.items():
        writer.writerow([key, value])
        
               
#print extractFolderName('/Users/Golnoosh/Documents/4c9fe29d6bea6d70c02b7eca7e2fac7b_en_50-64_male.xml')
#print cleanHtmlTags('&dsf; dsgfsd sdf sf asd asd asd $sd; &dfdsfdf;')
#print cleanSpams('sdfdf %f%dfg%df% djfj sfjkh asjh %20%fg%df%d%')

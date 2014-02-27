from CSVMaker import csvLineMaker
import os, csv

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

#Tranforms Mallet topic distribution output to normal row/column form
def fixMalletOutput(topicOutputPath, newPath, topic_num):

	#Convert .txt to appropriate .csv
	in_txt = csv.reader(open(topicOutputPath, "rb"), delimiter = '\t')
	output = csv.writer(open(newPath, 'wb'))

	next(in_txt, None)

	for row in in_txt:
		arr = [0] * (topic_num + 2)
		column_src = 0
		column_dst = 0

		file_info = row[1].split("_")
		arr[0] = file_info[2].split("/")[5]
		arr[1] = file_info[4] + " " + file_info[5].split(".")[0]

		for word in row[1:]:
			column_src = column_src + 1
			if column_src%2 == 0:
				column_dst = word
			else:
				arr[int(column_dst)+2] = word
				
		#arr.append("\n")
		output.writerow(arr)

	os.remove(topicOutputPath)
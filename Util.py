import os, csv
import numpy as np

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

#initDict("/home/jamarq/PAN/Data/cleaned")

from Run import cleanText
from Util import fixMalletOutput, fixMalletOutputInf
from KLDiv import outputDivergences
import os
import csv

'''
cleanText("../PAN14/blogs/en/","../blogs-en/Cleaned","../blogs-en/Grouped")
cleanText("../PAN14/blogs/es/","../blogs-es/Cleaned","../blogs-es/Grouped")
'''

'''
fixMalletOutputInf("../blogs-es/Topics/blogs-es-18-24-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-18-24-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-es/Topics/blogs-es-18-24_female-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-18-24_female-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-es/Topics/blogs-es-18-24_male-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-18-24_male-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-es/Topics/blogs-es-25-34-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-25-34-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-es/Topics/blogs-es-25-34_female-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-25-34_female-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-es/Topics/blogs-es-25-34_male-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-25-34_male-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-es/Topics/blogs-es-35-49-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-35-49-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-es/Topics/blogs-es-35-49_female-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-35-49_female-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-es/Topics/blogs-es-35-49_male-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-35-49_male-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-es/Topics/blogs-es-50-64-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-50-64-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-es/Topics/blogs-es-50-64_female-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-50-64_female-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-es/Topics/blogs-es-50-64_male-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-50-64_male-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-es/Topics/blogs-es-65-xx-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-65-xx-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-es/Topics/blogs-es-65-xx_female-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-65-xx_female-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-es/Topics/blogs-es-65-xx_male-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-65-xx_male-groupedtopics.csv",100)
fixMalletOutput("../blogs-es/Topics/blogs-es-alltopics.txt","../blogs-es/FixedTopics/blogs-es-alltopics.csv",100)
fixMalletOutputInf("../blogs-es/Topics/blogs-es-female-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-female-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-es/Topics/blogs-es-male-groupedtopics.txt","../blogs-es/FixedTopics/blogs-es-male-groupedtopics.csv",100)

fixMalletOutputInf("../blogs-en/Topics/blogs-en-18-24-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-18-24-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-en/Topics/blogs-en-18-24_female-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-18-24_female-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-en/Topics/blogs-en-18-24_male-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-18-24_male-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-en/Topics/blogs-en-25-34-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-25-34-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-en/Topics/blogs-en-25-34_female-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-25-34_female-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-en/Topics/blogs-en-25-34_male-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-25-34_male-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-en/Topics/blogs-en-35-49-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-35-49-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-en/Topics/blogs-en-35-49_female-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-35-49_female-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-en/Topics/blogs-en-35-49_male-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-35-49_male-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-en/Topics/blogs-en-50-64-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-50-64-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-en/Topics/blogs-en-50-64_female-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-50-64_female-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-en/Topics/blogs-en-50-64_male-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-50-64_male-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-en/Topics/blogs-en-65-xx-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-65-xx-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-en/Topics/blogs-en-65-xx_female-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-65-xx_female-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-en/Topics/blogs-en-65-xx_male-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-65-xx_male-groupedtopics.csv",100)
fixMalletOutput("../blogs-en/Topics/blogs-en-alltopics.txt","../blogs-en/FixedTopics/blogs-en-alltopics.csv",100)
fixMalletOutputInf("../blogs-en/Topics/blogs-en-female-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-female-groupedtopics.csv",100)
fixMalletOutputInf("../blogs-en/Topics/blogs-en-male-groupedtopics.txt","../blogs-en/FixedTopics/blogs-en-male-groupedtopics.csv",100)
'''

outputDivergences("../blogs-en/FixedTopics/blogs-en-allgroupedtopics.csv","../blogs-en/FixedTopics/blogs-en-alltopics.csv", "../blogs-en/blogs-en-divergences.csv")
outputDivergences("../blogs-es/FixedTopics/blogs-es-allgroupedtopics.csv","../blogs-es/FixedTopics/blogs-es-alltopics.csv", "../blogs-es/blogs-es-divergences.csv")

with open("../blogs-en/blogs-en-labels.csv", "wb") as label_doc:
	writer = csv.writer(label_doc)
	names = os.walk("../blogs-en/Cleaned")
	for dirpath, dirnames, filenames in names:
		for filename in filenames:
			writer.writerow([filename.split("_")[2]+" "+filename.split("_")[3].split(".")[0]])#+filename.split("_")[3].split["."][0]])

with open("../blogs-es/blogs-es-labels.csv", "wb") as label_doc:
	writer = csv.writer(label_doc)
	names = os.walk("../blogs-es/Cleaned")
	for dirpath, dirnames, filenames in names:
		for filename in filenames:
			writer.writerow([filename.split("_")[2]+" "+filename.split("_")[3].split(".")[0]])#+filename.split("_")[3].split["."][0]])

with open("../blogs-en/blogs-en-labels.csv") as label_doc, open("../blogs-en/blogs-en-divergences.csv") as div_doc,open("../blogs-en/blogs-en-divandlabels.csv","wb") as divandlabels:
	label_reader = csv.reader(label_doc)
	div_reader = csv.reader(div_doc)
	divandlabels_writer = csv.writer(divandlabels)

	labels = []
	header = ["label","id","div1","div2","div3","div4","div5","div6","div7","div8","div9","div10","div11","div12","div13","div14","div15","div16","div17"]

	divandlabels_writer.writerow(header)

	for line in label_reader:
		labels.append(line[0])

	counter = 0
	for line in div_reader:
		divandlabels_writer.writerow([labels[counter]] + line)
		counter+=1

with open("../blogs-es/blogs-es-labels.csv") as label_doc, open("../blogs-es/blogs-es-divergences.csv") as div_doc,open("../blogs-es/blogs-es-divandlabels.csv","wb") as divandlabels:
	label_reader = csv.reader(label_doc)
	div_reader = csv.reader(div_doc)
	divandlabels_writer = csv.writer(divandlabels)

	labels = []
	header = ["label","id","div1","div2","div3","div4","div5","div6","div7","div8","div9","div10","div11","div12","div13","div14","div15","div16","div17"]

	divandlabels_writer.writerow(header)

	for line in label_reader:
		labels.append(line[0])

	counter = 0
	for line in div_reader:
		divandlabels_writer.writerow([labels[counter]] + line)
		counter+=1

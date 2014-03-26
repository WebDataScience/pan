from Run import cleanText
from Util import fixMalletOutput, fixMalletOutputInf
from KLDiv import outputDivergences
import os
import csv

#cleanText("../PAN14/socialmedia/en/","../socmed-en/Cleaned","../socmed-en/Grouped")
#cleanText("../PAN14/socialmedia/es/","../socmed-es/Cleaned","../socmed-es/Grouped")

'''
fixMalletOutputInf("../socmed-es/Topics/socmed-es-18-24-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-18-24-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-es/Topics/socmed-es-18-24_female-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-18-24_female-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-es/Topics/socmed-es-18-24_male-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-18-24_male-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-es/Topics/socmed-es-25-34-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-25-34-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-es/Topics/socmed-es-25-34_female-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-25-34_female-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-es/Topics/socmed-es-25-34_male-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-25-34_male-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-es/Topics/socmed-es-35-49-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-35-49-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-es/Topics/socmed-es-35-49_female-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-35-49_female-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-es/Topics/socmed-es-35-49_male-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-35-49_male-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-es/Topics/socmed-es-50-64-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-50-64-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-es/Topics/socmed-es-50-64_female-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-50-64_female-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-es/Topics/socmed-es-50-64_male-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-50-64_male-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-es/Topics/socmed-es-65-xx-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-65-xx-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-es/Topics/socmed-es-65-xx_female-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-65-xx_female-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-es/Topics/socmed-es-65-xx_male-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-65-xx_male-groupedtopics.csv",100)
fixMalletOutput("../socmed-es/Topics/socmed-es-alltopics.txt","../socmed-es/FixedTopics/socmed-es-alltopics.csv",100)
fixMalletOutputInf("../socmed-es/Topics/socmed-es-female-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-female-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-es/Topics/socmed-es-male-groupedtopics.txt","../socmed-es/FixedTopics/socmed-es-male-groupedtopics.csv",100)

fixMalletOutputInf("../socmed-en/Topics/socmed-en-18-24-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-18-24-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-en/Topics/socmed-en-18-24_female-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-18-24_female-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-en/Topics/socmed-en-18-24_male-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-18-24_male-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-en/Topics/socmed-en-25-34-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-25-34-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-en/Topics/socmed-en-25-34_female-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-25-34_female-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-en/Topics/socmed-en-25-34_male-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-25-34_male-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-en/Topics/socmed-en-35-49-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-35-49-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-en/Topics/socmed-en-35-49_female-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-35-49_female-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-en/Topics/socmed-en-35-49_male-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-35-49_male-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-en/Topics/socmed-en-50-64-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-50-64-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-en/Topics/socmed-en-50-64_female-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-50-64_female-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-en/Topics/socmed-en-50-64_male-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-50-64_male-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-en/Topics/socmed-en-65-xx-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-65-xx-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-en/Topics/socmed-en-65-xx_female-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-65-xx_female-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-en/Topics/socmed-en-65-xx_male-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-65-xx_male-groupedtopics.csv",100)
fixMalletOutput("../socmed-en/Topics/socmed-en-alltopics.txt","../socmed-en/FixedTopics/socmed-en-alltopics.csv",100)
fixMalletOutputInf("../socmed-en/Topics/socmed-en-female-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-female-groupedtopics.csv",100)
fixMalletOutputInf("../socmed-en/Topics/socmed-en-male-groupedtopics.txt","../socmed-en/FixedTopics/socmed-en-male-groupedtopics.csv",100)
'''

outputDivergences("../socmed-en/FixedTopics/socmed-en-allgroupedtopics.csv","../socmed-en/FixedTopics/socmed-en-alltopics.csv", "../socmed-en/socmed-en-divergences.csv")
outputDivergences("../socmed-es/FixedTopics/socmed-es-allgroupedtopics.csv","../socmed-es/FixedTopics/socmed-es-alltopics.csv", "../socmed-es/socmed-es-divergences.csv")

with open("../socmed-en/socmed-en-labels.csv", "wb") as label_doc:
	writer = csv.writer(label_doc)
	names = os.walk("../socmed-en/Cleaned")
	for dirpath, dirnames, filenames in names:
		for filename in filenames:
			writer.writerow([filename.split("_")[2]+" "+filename.split("_")[3].split(".")[0]])#+filename.split("_")[3].split["."][0]])

with open("../socmed-es/socmed-es-labels.csv", "wb") as label_doc:
	writer = csv.writer(label_doc)
	names = os.walk("../socmed-es/Cleaned")
	for dirpath, dirnames, filenames in names:
		for filename in filenames:
			writer.writerow([filename.split("_")[2]+" "+filename.split("_")[3].split(".")[0]])#+filename.split("_")[3].split["."][0]])

with open("../socmed-en/socmed-en-labels.csv") as label_doc, open("../socmed-en/socmed-en-divergences.csv") as div_doc,open("../socmed-en/socmed-en-divandlabels.csv","wb") as divandlabels:
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

with open("../socmed-es/socmed-es-labels.csv") as label_doc, open("../socmed-es/socmed-es-divergences.csv") as div_doc,open("../socmed-es/socmed-es-divandlabels.csv","wb") as divandlabels:
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

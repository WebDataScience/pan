from Run import cleanText
from Util import fixMalletOutput, fixMalletOutputInf
from KLDiv import outputDivergences
import os
import csv


#cleanText("../PAN14/reviews/en/","../reviews-en/Cleaned","../reviews-en/Grouped")
#cleanText("../PAN14/reviews/es/","../reviews-es/Cleaned","../reviews-es/Grouped")


'''
fixMalletOutputInf("../reviews-es/Topics/reviews-es-18-24-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-18-24-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-es/Topics/reviews-es-18-24_female-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-18-24_female-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-es/Topics/reviews-es-18-24_male-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-18-24_male-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-es/Topics/reviews-es-25-34-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-25-34-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-es/Topics/reviews-es-25-34_female-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-25-34_female-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-es/Topics/reviews-es-25-34_male-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-25-34_male-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-es/Topics/reviews-es-35-49-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-35-49-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-es/Topics/reviews-es-35-49_female-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-35-49_female-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-es/Topics/reviews-es-35-49_male-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-35-49_male-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-es/Topics/reviews-es-50-64-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-50-64-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-es/Topics/reviews-es-50-64_female-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-50-64_female-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-es/Topics/reviews-es-50-64_male-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-50-64_male-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-es/Topics/reviews-es-65-xx-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-65-xx-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-es/Topics/reviews-es-65-xx_female-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-65-xx_female-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-es/Topics/reviews-es-65-xx_male-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-65-xx_male-groupedtopics.csv",100)
fixMalletOutput("../reviews-es/Topics/reviews-es-alltopics.txt","../reviews-es/FixedTopics/reviews-es-alltopics.csv",100)
fixMalletOutputInf("../reviews-es/Topics/reviews-es-female-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-female-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-es/Topics/reviews-es-male-groupedtopics.txt","../reviews-es/FixedTopics/reviews-es-male-groupedtopics.csv",100)

fixMalletOutputInf("../reviews-en/Topics/reviews-en-18-24-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-18-24-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-en/Topics/reviews-en-18-24_female-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-18-24_female-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-en/Topics/reviews-en-18-24_male-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-18-24_male-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-en/Topics/reviews-en-25-34-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-25-34-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-en/Topics/reviews-en-25-34_female-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-25-34_female-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-en/Topics/reviews-en-25-34_male-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-25-34_male-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-en/Topics/reviews-en-35-49-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-35-49-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-en/Topics/reviews-en-35-49_female-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-35-49_female-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-en/Topics/reviews-en-35-49_male-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-35-49_male-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-en/Topics/reviews-en-50-64-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-50-64-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-en/Topics/reviews-en-50-64_female-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-50-64_female-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-en/Topics/reviews-en-50-64_male-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-50-64_male-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-en/Topics/reviews-en-65-xx-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-65-xx-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-en/Topics/reviews-en-65-xx_female-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-65-xx_female-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-en/Topics/reviews-en-65-xx_male-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-65-xx_male-groupedtopics.csv",100)
fixMalletOutput("../reviews-en/Topics/reviews-en-alltopics.txt","../reviews-en/FixedTopics/reviews-en-alltopics.csv",100)
fixMalletOutputInf("../reviews-en/Topics/reviews-en-female-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-female-groupedtopics.csv",100)
fixMalletOutputInf("../reviews-en/Topics/reviews-en-male-groupedtopics.txt","../reviews-en/FixedTopics/reviews-en-male-groupedtopics.csv",100)
'''

outputDivergences("../reviews-en/FixedTopics/reviews-en-allgroupedtopics.csv","../reviews-en/FixedTopics/reviews-en-alltopics.csv", "../reviews-en/reviews-en-divergences.csv")
#outputDivergences("../reviews-es/FixedTopics/reviews-es-allgroupedtopics.csv","../reviews-es/FixedTopics/reviews-es-alltopics.csv", "../reviews-es/reviews-es-divergences.csv")

with open("../reviews-en/reviews-en-labels.csv", "wb") as label_doc:
	writer = csv.writer(label_doc)
	names = os.walk("../reviews-en/Cleaned")
	for dirpath, dirnames, filenames in names:
		for filename in filenames:
			writer.writerow([filename.split("_")[2]+" "+filename.split("_")[3].split(".")[0]])#+filename.split("_")[3].split["."][0]])
'''
with open("../reviews-es/reviews-es-labels.csv", "wb") as label_doc:
	writer = csv.writer(label_doc)
	names = os.walk("../reviews-es/Cleaned")
	for dirpath, dirnames, filenames in names:
		for filename in filenames:
			writer.writerow([filename.split("_")[2]+" "+filename.split("_")[3].split(".")[0]])#+filename.split("_")[3].split["."][0]])
'''
with open("../reviews-en/reviews-en-labels.csv") as label_doc, open("../reviews-en/reviews-en-divergences.csv") as div_doc,open("../reviews-en/reviews-en-divandlabels.csv","wb") as divandlabels:
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
'''
with open("../reviews-es/reviews-es-labels.csv") as label_doc, open("../reviews-es/reviews-es-divergences.csv") as div_doc,open("../reviews-es/reviews-es-divandlabels.csv","wb") as divandlabels:
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
'''

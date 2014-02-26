#!/usr/bin/python2.7

import TopicModeler, DivDictMaker, csv
from Util import initDict

def makeDivCSV(input_path, output_path):

	topic_num = 3
	#18-24, 25-34, 35-49, 50-64, 65+ <--PAN 14 labels
	labels = ["18-24_male", "18-24_female", "25-34_male", "25-34_female", "35-49_male", "35-49_female", "50-64_male", "50-64_female", "65-xx_male", "65-xx_female"]

	arr = DivDictMaker.getDivAtDir(input_path, topic_num, labels)

	csvfile = open(output_path+".csv", 'wb')
	writer = csv.writer(csvfile)

	for keys, values in arr.iteritems():
		data = values[1]+[values[0]]
		#print data
		writer.writerow(data)

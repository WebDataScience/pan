#!/usr/bin/python2.7

import argparse, TopicModeler, os, csv
from shutil import rmtree
from PreProcessor import clean
from LabelCollector import groupLabels, concatFiles
from KLDiv import outputDivergences
from Util import initDict

def getDivAtDir(src, topics, label_list):

	input_path = src
	topic_num = topics
	labels = label_list
	key_list = []

	div_dict = initDict(input_path)
	for key, value in div_dict.iteritems():
		key_list.append(key)
	
	if os.path.exists("../Data/cleaned"):
		rmtree("../Data/cleaned")
	os.makedirs("../Data/cleaned")

	clean(input_path,"../Data/cleaned")
	TopicModeler.inferTopicsTesting("../Data/cleaned", topic_num)
	
	in_txt = csv.reader(open("./malletstuff/alldocs.csv", "rb"), delimiter = '\t')
	output = csv.writer(open("./malletstuff/alldocs1.csv", 'wb'))
	'''
	index = 0
	for row in in_txt:
		temparr = [key_list[index]] + row[0].split(",")
		output.writerow(temparr)
		index+=1
	'''

	for label in labels:
		print "getting divergences for " + label + " in test"
		div_info = outputDivergences("./malletstuff/"+label+"topics_total.csv","./malletstuff/alldocs.csv","./malletstuff/"+label+"_divergences.csv",True)
		index = 0
		for key, value in div_info.iteritems():
			div_dict[key_list[index]][1].append(div_info[key])
			index+=1

	#print div_dict
	return div_dict

#getDivAtDir("../Data/cleaned","blah",["18-24_male", "18-24_female", "25-34_male", "25-34_female", "35-49_male", "35-49_female", "50-64_male", "50-64_female", "65-xx_male", "65-xx_female"])
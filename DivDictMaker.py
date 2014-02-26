#!/usr/bin/python2.7

import argparse, TopicModeler, os
from shutil import rmtree
from PreProcessor import clean
from LabelCollector import groupLabels, concatFiles
from KLDiv import outputDivergences
from Util import initDict

def getDivAtDir(src, topics, label_list):

	input_path = src
	topic_num = topics
	labels = label_list

	div_dict = initDict(input_path)
	#print div_dict

	# todo for each subdirectory name

	if os.path.exists("../Data/cleaned"):
		rmtree("../Data/cleaned")
	os.makedirs("../Data/cleaned")

	clean(input_path,"../Data/cleaned")
	TopicModeler.modelTopics("../Data/cleaned", topic_num)
	groupLabels("../Data/cleaned","../Data/grouped",labels)
	for label in labels:
		concatFiles("../Data/grouped/"+label)
		TopicModeler.inferTopics(label, topic_num)

	for label in labels:
		div_info = outputDivergences("./malletstuff/"+label+"topics_total.csv","./malletstuff/alldocs.csv","./malletstuff/"+label+"_divergences.csv")
		for key, value in div_info.iteritems():
			div_dict[key][1].append(div_info[key])

	return div_dict

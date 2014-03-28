import csv, os, subprocess
from KLDiv import calcKLDiv
from Util import fixMalletOutput, fixMalletOutputInf

def extractTopicFeatures(input_path, topic_num, language, type):
	if not os.path.exists("./malletstuff"):
		os.makedirs("./malletstuff")

	group = language+"_"+type

	args=['./traintopics.sh', input_path, str(topic_num), group]
	subprocess.call(args)
	return fixMalletOutput("./malletstuff/"+group+"-alldocs.txt", "./malletstuff/"+group+"-alldocs.csv", topic_num)

def extractTopicFeaturesTesting(input_path, topic_num, language, type):
	group = language+"_"+type

	args=['./infertopicstest.sh', input_path, "./malletstuff/testing-topics.csv","./malletstuff/"+group+"-topic-inferencer.inf"]
	subprocess.call(args)
	return fixMalletOutputInf("./malletstuff/testing-topics.csv", "./malletstuff/testing-topics.csv", topic_num)

def klDiv(topic_dic, groupPath,labels,topic_num,group):
	group_list = []
	for label in labels:
		group_list.append(extractGroupTopics(groupPath+"/"+label+".txt",group,topic_num,label))
		extractGroupTopics(groupPath+"/"+label+".txt",group,topic_num,label)

	subprocess.call("cat ./malletstuff/*fixed.csv > ./malletstuff/"+group+"-all-labels.csv", shell = True)
	
	group_list = []

	with open("./malletstuff/"+group+"-alllabels.csv") as alllabels_in:
		alllabels_reader = csv.reader(alllabels_in)

		for line in alllabels_reader:
			group_list.append(line)

	ret_dict = {}

	for keys, values in topic_dic.iteritems():
		dist = []
		for index in range(0,len(labels)):
			dist.append(calcKLDiv(group_list[index],values))
		ret_dict[keys] = dist

	return ret_dict

def klDivTesting(topic_dic, groupPath,labels,topic_num,group):
	group_list = []

	with open("./malletstuff/"+group+"-alllabels.csv") as alllabels_in:
		alllabels_reader = csv.reader(alllabels_in)

		for line in alllabels_reader:
			group_list.append(line)

	ret_dict = {}

	for keys, values in topic_dic.iteritems():
		dist = []
		for index in range(0,len(labels)):
			dist.append(calcKLDiv(group_list[index],values))
		ret_dict[keys] = dist

	return ret_dict


def extractGroupTopics(groupPath,group,topic_num,label):
	args=['./infertopics.sh', groupPath, "./malletstuff/" + label + "-topics.csv","./malletstuff/"+group+"-topic-inferencer.inf"]
	subprocess.call(args)
	fixMalletOutputInf("./malletstuff/" + label + "-topics.csv", "./malletstuff/" + label + "-topics-fixed.csv", topic_num)
	#return fixMalletOutputInf("./malletstuff/"+label+"-topics.csv", "./malletstuff/"+label+"-topics.csv", topic_num)



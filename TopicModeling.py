import csv
from KLDiv import calcKLDiv

def extractTopicFeatures(input_path, topic_num, language, type):
	if not os.path.exists("./malletstuff"):
		os.makedirs("./malletstuff")

	group = language+"_"+type

	args=['./traintopics.sh', src, str(topic_num), group]
	subprocess.call(args)
	return fixMalletOutput("./malletstuff/alldocs.txt", "./malletstuff/alldocs.csv", topic_num)

def klDiv(topic_dic, groupPath,labels):
	group_list = []
	for label in labels:
		group_list.append(extractGroupTopics(groupPath+"/"+label+".txt",label))

	index = 0

	for keys, values in topic_dic.iteritems():
		print calcKLDiv(group_list[index],values)

def extractGroupTopics(groupPath,label):
	args=['./infertopics.sh', groupPath, "./malletstuff/" + label + "-topics.csv","./malletstuff/"+label+"-topic-inferencer.inf"]
	subprocess.call(args)
	#fixMalletOutput("./malletstuff/" + label + "topics.csv", "./malletstuff/" + label + "topics.csv", topic_num)
	return fixMalletOutputInf("./malletstuff/"+label+"topics.csv", "./malletstuff/"+label+"topics.csv", topic_num)



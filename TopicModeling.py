import csv

def extractTopicFeatures(input_path, topic_num, language, type):
	if not os.path.exists("./malletstuff"):
		os.makedirs("./malletstuff")

	group = language+type

	args=['./traintopics.sh', src, str(topic_num), group]
	subprocess.call(args)
	fixMalletOutput("./malletstuff/alldocs.txt", "./malletstuff/alldocs.csv", topic_num)
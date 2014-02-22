import os, subprocess
from Util import fixMalletOutput, fixMalletOutputInf

def modelTopics(src, topic_num):

	if not os.path.exists("./malletstuff"):
		os.makedirs("./malletstuff")

	args=['./traintopics.sh', src, str(topic_num)]
	#subprocess.call(args)
	fixMalletOutput("./malletstuff/alldocs.txt", "./malletstuff/alldocs.csv", topic_num)

def inferTopics(label, topic_num):
	print label
	args=['./infertopics.sh', "../Data/grouped/" + label + "/result.txt", "./malletstuff/" + label + "topics.csv"]
	subprocess.call(args)
	#fixMalletOutput("./malletstuff/" + label + "topics.csv", "./malletstuff/" + label + "topics.csv", topic_num)
	fixMalletOutputInf("./malletstuff/"+label+"topics.csv", "./malletstuff/"+label+"topics_total.csv", 10)

#modelTopics("/home/jamarq/PAN/Data/grouped/10s_male",10)
#modelTopics("/home/jamarq/PAN/Data/cleaned", 10)
#inferTopics("10s_male", 10)
from nltk.tag.stanford import POSTagger
from os import listdir
from os.path import isfile, join

#Build dictionary of tags from 
def getTags(src):

	ret_arr = dict()

	only_files = [ f for f in listdir(src) if isfile(join(src,f)) ]
	for entry in only_files:

		doc_arr = dict()
		
		read_file = open(src+"/"+entry, "rb")
		contents = read_file.read()
		st = None
		if entry.split("_")[1] == "en":
			st = POSTagger('./stanford-postagger-full-2014-01-04/models/english-bidirectional-distsim.tagger','stanford-postagger-full-2014-01-04/stanford-postagger.jar')
		else:
			st = POSTagger('./stanford-postagger-full-2014-01-04/models/english-bidirectional-distsim.tagger','stanford-postagger-full-2014-01-04/stanford-postagger.jar')

		ret = st.tag(contents.split())

		for tag in ret:
			if tag[1] in doc_arr:
				doc_arr[tag[1]]+=1
			else:
				doc_arr[tag[1]]=1

		ret_arr[entry.split("_")[0]]=doc_arr
		print ret_arr
	
	return ret_arr

#getTags("/home/jamarq/PAN/Data/cleaned")
from bs4 import BeautifulSoup
import os

def getDocType(src):
	soup = BeautifulSoup(open(src))
	return soup.author['type']+"-"+soup.author['lang']

def listAllFiles(src):
	for root, subFolders, files in os.walk(src):
		for file in files:
			print os.path.abspath(os.path.join(root, file))

def getLeaves(src):
	leaves=[]
	for root, subFolders, files in os.walk(src):
		if len(subFolders)==0:
			leaves.append(root)
	print len(leaves)
	return leaves

#getDocType("/home/jamarq/PAN/Data/PAN14/PAN14/pan14-author-profiling-training-corpus-blogs-2014-02-10/en/fe826c2665b9aecd0e77a27eaa21e1d5_en_35-49_male.xml")
#listAllFiles("/home/jamarq/PAN/Data/PAN14/PAN14")
getLeaves("/home/jamarq/PAN/Data/PAN14/PAN14")
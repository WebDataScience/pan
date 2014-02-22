from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
import re

def countTags(src):
	ret_arr = dict()

	only_files = [ f for f in listdir(src) if isfile(join(src,f)) ]
	for entry in only_files:
		doc_arr = dict()
		soup = BeautifulSoup(open(src+"/"+entry,"rb"))

		doc_arr["links"] = len(soup.find_all('a'))
		doc_arr["image"] = len(soup.find_all('img'))
		doc_arr["bold"] = len(soup.find_all('b'))
		doc_arr["italic"] = len(soup.find_all('i'))
		doc_arr["lists"] = len(soup.find_all('ul')) + len(soup.find_all('ol'))

		ret_arr[entry.split("_")[0]]=doc_arr

	print ret_arr
	return ret_arr	

#countTags("/home/jamarq/PAN/Data/PAN14/PAN14/pan14-author-profiling-training-corpus-blogs-2014-02-10/en")
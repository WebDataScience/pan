from os import listdir
from os.path import isfile, join
import re

def countTags(src):
	ret_arr = dict()

	only_files = [ f for f in listdir(src) if isfile(join(src,f)) ]
	for entry in only_files:
		doc_arr = dict()
		
		read_file = open(src+"/"+entry, "rb")
		contents = read_file.read()

		links = re.compile('<a href')
		images = re.compile('<img')
		bold = re.compile('<b')
		italic = re.compile('<i')
		lists = re.compile('((<ul)|(<ol))')
		
		doc_arr['links'] = len(links.findall(contents))
		doc_arr['images'] = len(images.findall(contents))
		doc_arr['bold'] = len(bold.findall(contents))
		doc_arr['italic'] = len(italic.findall(contents))
		doc_arr['lists'] = len(lists.findall(contents))

		ret_arr[entry.split("_")[0]]=doc_arr
		print ret_arr
	
	return ret_arr

countTags("/home/jamarq/PAN/Data/PAN14/PAN14/pan14-author-profiling-training-corpus-blogs-2014-02-10/en")
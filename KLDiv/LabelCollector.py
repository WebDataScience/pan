from os import listdir
from os.path import isfile, join
from shutil import copy, rmtree
import os, re

def groupLabels(src, dst, labels):

	print "Grouping documents"

	if os.path.exists(dst):
		rmtree(dst)
	else:
		os.makedirs(dst)

	for label in labels:
		makeFolders(dst + "/" + label)

	onlyfiles = [ f for f in listdir(src) if isfile(join(src,f)) ]

	for entry in onlyfiles:
		fileinfo = entry.split("_")
		copy(src + "/" + entry, dst + "/" + (fileinfo[2] + " " + fileinfo[3].split(".")[0]).replace(' ', '_') + "/" + entry)

def concatFiles(src):
	onlyfiles = [ f for f in listdir(src) if isfile(join(src,f)) ]

	data = ""

	for entry in onlyfiles:
        
		with open (src + "/" + entry, "r") as myfile:
			data += myfile.read()

	file(src + "/result.txt","wb").write(data)

def makeFolders(dst):
	if not os.path.exists(dst):
		os.makedirs(dst)

#groupLabels("../Data/cleaned/", "../Data/grouped", ["10s_male", "10s_female", "20s_male", "20s_female", "30s_male", "30s_female"])
#concatFiles("../Data/grouped/10s_male")
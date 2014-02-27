from HTMLParser import HTMLParser
from os import listdir
from os.path import isfile, join
from shutil import copy
import os, re

def groupLabels(src, dst, labels):

	for label in labels:
		makeFolders(dst + "/" + label)

	onlyfiles=[f for f in listdir(src) if isfile(join(src,f))]

    for entry in onlyfiles:
    	fileinfo = entry.split("_")
    	copy(src + "/" + entry, dst + "/" + fileinfo[2] + " " + fileinfo[2] + "/" + entry)

def makeFolders(dst):
	if not os.path.exists(dst):
        os.makedirs(dst)

groupLabels("../Data/subset_training1", "../Data/grouped", ["10s male", "10s female", "20s male", "20s female", "30s male", "30s female"])
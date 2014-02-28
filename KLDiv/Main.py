#!/usr/bin/python2.7
import argparse, DivCSVMaker, os, DivCSVMaker, SVMRunner
from shutil import rmtree

def getLeaves(src):
	leaves=[]
	for root, subFolders, files in os.walk(src):
		if len(subFolders)==0:
			leaves.append(root)
	print len(leaves)
	return leaves

parser = argparse.ArgumentParser(description='Trains a model')
parser.add_argument('-i','--input',help='Path to training corpus',required=True)
parser.add_argument('-o','--output',help='Path to output directory',required=True)
parser.add_argument('-t','--testing',help='Path to testing corpus',required=True)
parser.add_argument('-l','--language',help='Language of corpus',required=True)
parser.add_argument('-g','--doctype',help='Type of documents (blogs, reiviews, etc.)',required=True)
args = parser.parse_args()
	
input_path = args.input
output_path = args.output
testing_path = args.testing
language = args.language
doctype = args.doctype

paths = getLeaves(input_path)

if os.path.exists(output_path):
	rmtree(output_path)
os.makedirs(output_path)

for path in paths:
	#fileinfo = path.split("/")
	#src_type = fileinfo[-1] + "_" + fileinfo[-2].split("-")[5]
	#if src_type != language+"_"+doctype:
	#	continue
	final_out = output_path +"/topicdiv-10-1tra"
	DivCSVMaker.makeDivCSV(path, final_out)

paths = getLeaves(testing_path)

for path in paths:
	#fileinfo = path.split("/")
	#src_type = fileinfo[-1] + "_" + fileinfo[-2].split("-")[5]
	#if src_type != language+"_"+doctype:
	#	continue
	final_out = output_path +"/topicdiv-10-1tst"
	DivCSVMaker.makeDivCSV(path, final_out, True)

#predictions = SVMRunner.runSVM(output_path+"/topicdiv-10-1tra.csv", output_path+"/topicdiv-10-1tst.csv")
#print predictions

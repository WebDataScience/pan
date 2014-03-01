#!/usr/bin/python2.7
import argparse, DivCSVMaker, os, DivCSVMaker
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
args = parser.parse_args()
	
input_path = args.input
output_path = args.output

paths = getLeaves(input_path)

if os.path.exists(output_path):
	rmtree(output_path)
os.makedirs(output_path)

for path in paths:
	fileinfo = path.split("/")
	src_type = fileinfo[-1] + "_" + fileinfo[-2].split("-")[5]
	#final_out = output_path+"/"+src_type
	final_out = output_path +"/"+src_type

	print src_type
	print path
	DivCSVMaker.makeDivCSV(path, final_out)

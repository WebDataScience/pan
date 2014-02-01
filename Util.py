from shutil import copy
from sklearn.cross_validation import KFold
from CSVMaker import csvLineMaker
import os, csv

#Save textual content to a file
#Input: file path and textual content
def saveFile (path, content):
    file(path,"wb").writelines(content)

#Extract files from the folder
def getFilesFromFolder(folderPath):
    files = [f for f in os.listdir(folderPath) if f.endswith('.xml')]
    return files
#Read content of the file    
def readFile(filePath):
    text = open(filePath, 'r').read()
    return text

def saveFolder(folderPath):  
    if not os.path.exists(folderPath):
        os.makedirs(folderPath) 

#Splits an input .csv by 10 folds by line into .csv's 
def tenFoldSplitCSV(src_csv, dst_path):
	with open(src_csv, 'rb') as csvfile:
		if not os.path.exists(dst_path):
			os.makedirs(dst_path)
		length = 0
		lines = []
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			lines.append(row)
			length+=1
		kf = KFold(length, n_folds = 10)
		dir_iter = 1
		for train, test in kf:
			foldcsv = "Train\n"			
			for train_index in train:
				foldcsv = foldcsv + csvLineMaker(lines[train_index]) + "\n"
			foldcsv = foldcsv + "Test\n"
			for test_index in test:
				foldcsv = foldcsv + csvLineMaker(lines[train_index]) + "\n"
			saveFile(dst_path + "fold" + str(dir_iter) + ".csv", foldcsv)
			dir_iter+=1

#Split data in directory into 10 folds.
###Not an efficient solution###
def tenFoldSplitDir(src_path, dst_path):
	files = getFilesFromFolder(src_path)
	kf = KFold(len(files), n_folds = 10)

	dir_iter = 1

	for train, test in kf:
		
		train_dest = dst_path + "train-set" + str(dir_iter) + "/"
		test_dest = dst_path + "test-set" + str(dir_iter) + "/"

		if not os.path.exists(train_dest):
			os.makedirs(train_dest)
		if not os.path.exists(test_dest):
			os.makedirs(test_dest)

		for train_index in train:
			copy(src_path + files[train_index], train_dest)
		for test_index in test:
			copy(src_path + files[test_index], test_dest)

		dir_iter+=1

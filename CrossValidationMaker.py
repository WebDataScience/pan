from Util import getFilesFromFolder, saveFile
from shutil import copy
from sklearn.cross_validation import KFold, StratifiedKFold
from CSVMaker import csvLineMaker
from numpy import genfromtxt
import os, csv

#Creates stratified folds according to the proportion of labels
def stratCrossVal(src, dst, fold_num):
	folds = []
	data = []
	labels = []

	if not os.path.exists(dst):
		os.makedirs(dst)

	with open(src, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		for row in reader:
			data.append(row)
			labels.append(row[1])

		skf = StratifiedKFold(labels, fold_num)
	
	index = 1
	for train, test in skf:
		out_csv = csv.writer(open(dst + "fold" + str(index) + ".csv", 'wb'))
		for num in train:
			out_csv.writerow(data[num])
		for num in test:
			out_csv.writerow(data[num])
		index = index + 1



#Separates data into test/train and validation portions
'''
def validationSeparate(src_csv, dst_path, proportion_validation):
	with open(src_csv, 'rb') as csvfile:
		count = 0
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			lines.append(row)
			count = count + 1
		test-train = count * (1-proportion_validation)
		testtraincsv = ""
		validationcsv = ""
		for testtrain_index in range(0,test-train)
			testtraincsv = testtraincsv + csvLineMaker(lines[testtrain_index]) + "\n"
		for validation_index in range(test-train,count)
			validationcsv = validationcsv + csvLineMaker(lines[validation_csv]) + "\n"

		saveFile(dst_path + "testtrain.csv", testtraincsv)
		saveFile(dst_path + "validation.csv", validationcsv)	
'''

#Splits an input .csv by 10 folds by line into .csv 
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

stratCrossVal("/Users/the_james_marq/PAN/outputs/9Feb14-100topics-236602docs/test_composition.csv", "/Users/the_james_marq/PAN/outputs/9Feb14-100topics-236602docs/folds/", 10)
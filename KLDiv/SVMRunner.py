from sklearn import svm
import csv

def runSVM(train, test):
	testdata = csv.reader(open(test, "rb"))
	traindata = csv.reader(open(train, "rb"))

	traindata_arr = []
	trainlabels_arr = []
	testdata_arr = []
	for row in traindata:
		traindata_arr.append(row[:-1])
		trainlabels_arr.append(row[-1])

	for row in testdata:
		testdata_arr.append(row[:-1])

	X = [[0, 0], [1, 1]]
	y = [0, 1]
	clf = svm.SVC()

	clf.fit(traindata_arr, trainlabels_arr)

	return clf.predict(testdata_arr)

#runSVM("./outputs/train.csv", "./outputs/train.csv")
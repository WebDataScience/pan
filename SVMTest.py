from sklearn import svm
import csv

#Test for SVM
def classifyDocs(src):
	with open(src,'rb') as data:
		reader = data.readlines()

		train_data = []
		train_labels = []
		test_data = []
		test_labels = []

		count = 0
		train = True
		length = 0

		for lines in reader:
			length = length + 1

		for lines in reader:
			count = count + 1 
			if count == 1:
				continue
			elif count == int(length*0.9):
				train = False
				continue
			elif train:
				train_list = []
				for num in lines.split(","):
					if num == lines.split(",")[0] or num == lines.split(",")[1] or num == "\n":
						continue
					else:
						ins_num = num.replace("\"","").lower()
						train_list.append(float(ins_num))
				train_data.append(train_list)
				train_labels.append(lines.split(",")[1])
			else:
				test_list= []
				for num in lines.split(","):
					if num == lines.split(",")[0] or num == lines.split(",")[1] or num == "\n":
						continue
					else:
						ins_num = num.replace("\"", "").lower()
						test_list.append(float(ins_num))
				test_data.append(test_list)
				test_labels.append(lines.split(",")[1])

		clf = svm.SVC(kernel = 'linear')
		clf.fit(train_data,train_labels)

		results =0
		true = 0 
		false = 0

		for lines in test_data:
			prediction = clf.predict(lines)[0]
			if prediction==test_labels[results]:
				true = true + 1
			else:
				false = false + 1
			results = results + 1

		print "Accuracy: " + str(true/float(results))

for i in range(1, 11):
	classifyDocs("/Users/the_james_marq/PAN/outputs/9Feb14-100topics-236602docs/folds/fold"+str(i)+".csv")
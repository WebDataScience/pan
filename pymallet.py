import subprocess, os
import csv

import subprocess, os
import csv

#Call the mallet script
subprocess.call("./callmallet.sh")

txt_file = r"./outputs/composition.txt"
csv_file = r"./outputs/composition.csv"
other_csv = r"./outputs/test_composition.csv"

#Convert .txt to appropriate .csv
in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'wb'))
other_out = csv.writer(open(other_csv, 'wb'))

'''
for row in in_txt:
	arr = [0] * 100
	row[0] = arr [0]
	for i in range(1,200):
		if i%2 != 0:
			continue
		else:
			arr[row[i]/2] = row[i-1]
	other_out.csv.writerow(arr)
'''
next(in_txt, None)
header = ["ID", "Label"]

for i in range(1,20+1):
	header.append("Topic " + str(i))

other_out.writerow(header)

for row in in_txt:
	arr = [0] * 22
	column_src = 0
	column_dst = 0

	file_info = row[1].split("_")
	arr[0] = file_info[3].split("/")[1]
	arr[1] = file_info[5] + " " + file_info[6].split(".")[0]

	for word in row[1:]:
		column_src = column_src + 1
		if column_src%2 == 0:
			column_dst = word
		else:
			arr[int(column_dst)+2] = word
			
	#arr.append("\n")
	other_out.writerow(arr)

os.remove("./outputs/composition.txt")


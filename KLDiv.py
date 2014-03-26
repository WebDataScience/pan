import numpy as np
from math import exp
import csv

def getDistributions(path, group_flag=False):
	with open(path, "rb") as infile:
		in_txt = csv.reader(infile)
		arr = []	
		for row in in_txt: 
			if group_flag:
				arr.append(row)
			else:
				arr.append([row[0], row[1:]])
		return arr

def calcKLDiv(dist_1, dist_2):
	dist_1 = np.asarray(dist_1, dtype=np.float)
	dist_2 = np.asarray(dist_2, dtype=np.float)

	return np.sum(np.where(dist_1 != 0, dist_1 * np.log(dist_1/dist_2), 0))

def avKLDiv(dist_1, dist_2):

	dist_1 = np.asarray(dist_1, dtype=np.float)
	dist_2 = np.asarray(dist_2, dtype=np.float)

	p1 = np.dot(dist_1,(1/(dist_1 + dist_2)))
	p2 = np.dot(dist_2,(1/(dist_1 + dist_2)))
	m = p1*dist_1 + p2*dist_2

	return p1*calcKLDiv(dist_1,m) + p2*calcKLDiv(dist_2,m)

def outputDivergences(concat_path, total_path, out_path):
	with open(out_path, "wb") as outfile:
		out_txt = csv.writer(outfile)

		concat_dist = getDistributions(concat_path, True)
		total_dist = getDistributions(total_path)

		ret_dict = dict()

		for entry in total_dist:
			#print avKLDiv(concat_dist[0],entry[1])
			div_arr = []
			div_arr.append(entry[0])
			for line in concat_dist:
				div_arr.append(calcKLDiv(line, entry[1]))

			out_txt.writerow(div_arr)
			ret_dict[entry[0]] = calcKLDiv(concat_dist[0],entry[1])

		return ret_dict


'''
q = getDistributions("/home/jamarq/PAN/KLDiv/malletstuff/alldocs.csv")
p = getDistributions("/home/jamarq/PAN/KLDiv/malletstuff/10s_maletopics_total.csv",True)

for entry in q:
	print avKLDiv(entry,p[0])
'''
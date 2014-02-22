#!/usr/bin/python2.7
import argparse, PreProcessor, LabelCollector, TopicModeler, KLDiv

parser = argparse.ArgumentParser(description='Trains a model')
parser.add_argument('-i','--input',help='Path to training corpus',required=True)
parser.add_argument('-o','--output',help='Path to output directory',required=True)
args = parser.parse_args()

input_path = args.input
output_path = args.output

topic_num = 10
#18-24, 25-34, 35-49, 50-64, 65+
labels = ["18-24_male", "18-24_female", "25-34_male", "25-34_female", "35-49_male", "35-49_female", "50-64_male", "50-64_female", "65-xx_male", "65-xx_female"]

# todo for each subdirectory name

PreProcessor.clean(input_path,"../Data/cleaned")
TopicModeler.modelTopics("../Data/cleaned", topic_num)
LabelCollector.groupLabels("../Data/cleaned","../Data/grouped",labels)
for label in labels:
	LabelCollector.concatFiles("../Data/grouped/"+label)
	TopicModeler.inferTopics(label, topic_num)
for label in labels:
	KLDiv.outputDivergences("./malletstuff/"+label+"topics_total.csv","./malletstuff/alldocs.csv","./malletstuff/"+label+"_divergences.csv")
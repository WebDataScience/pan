#!/usr/bin/python2.7
import argparse, PreProcessor, LabelCollector, TopicModeler, KLDiv

parser = argparse.ArgumentParser(description='Trains a model')
parser.add_argument('-i','--input',help='Path to training corpus',required=True)
parser.add_argument('-o','--output',help='Path to output directory',required=True)
args = parser.parse_args()

input_path = args.input
output_path = args.output

topic_num = 10
labels = ["10s_male", "10s_female", "20s_male", "20s_female", "30s_male", "30s_female"]

PreProcessor.clean(input_path,"../Data/cleaned")
TopicModeler.modelTopics("../Data/cleaned", topic_num)
LabelCollector.groupLabels("../Data/cleaned","../Data/grouped",labels)
for label in labels:
	LabelCollector.concatFiles("../Data/grouped/"+label)
	TopicModeler.inferTopics(label, topic_num)

for label in labels:
	KLDiv.outputDivergences("./malletstuff/"+label+"topics_total.csv","./malletstuff/alldocs.csv","./malletstuff/"+label+"_divergences.csv")
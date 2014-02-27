#!/usr/bin/python2.7
import argparse, subprocess
from Util import fixMalletOutput
#from Main.py import doPreProcessingAndTraining

parser = argparse.ArgumentParser(description='Trains a model')
parser.add_argument('-i','--input',help='Path to training corpus',required=True)
parser.add_argument('-o','--output',help='Path to output directory',required=True)
args = parser.parse_args()

input_path = args.input
output_path = args.output

topic_num = '10'

args=['./modeltopics.sh', input_path, topic_num]

subprocess.call(args)

fixMalletOutput("input-composition.txt", "input-topic-model.csv", 10)
#doPreProcessingAndTrainint(input_path)

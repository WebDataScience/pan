#!/bin/bash

export _JAVA_OPTIONS='-Xmx6g'
#/Users/the_james_marq/Desktop/mallet-2.0.7/bin/mallet import-dir --input /Users/the_james_marq/PAN/Data/pan13-author-profiling-training-corpus-2013-01-09/en --output /Users/the_james_marq/PAN/outputs/tokens.mallet --keep-sequence --remove-stopwords
/Users/the_james_marq/Desktop/mallet-2.0.7/bin/mallet train-topics  --input /Users/the_james_marq/PAN/outputs/tokens.mallet  --num-topics 20 --optimize-interval 20 --output-state /Users/the_james_marq/PAN/outputs/topic-state.gz  --output-topic-keys /Users/the_james_marq/PAN/outputs/keys.txt --output-doc-topics /Users/the_james_marq/PAN/outputs/composition.txt

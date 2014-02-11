#!/bin/bash

export _JAVA_OPTIONS='-Xmx6g'
#./mallet-2.0.7/bin/mallet import-dir --input ../Data/pan13-author-profiling-training-corpus-2013-01-09/en --output ../outputs/tokens.mallet --keep-sequence --remove-stopwords
./mallet-2.0.7/bin/mallet train-topics  --input ../outputs/tokens.mallet  --num-topics 10 --optimize-interval 20 --output-state ../outputs/topic-state.gz  --output-topic-keys ../outputs/keys.txt --output-doc-topics ../outputs/composition.txt

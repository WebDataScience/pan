#!/bin/bash

#export _JAVA_OPTIONS='-Xmx3g'
./mallet-2.0.7/bin/mallet import-dir --input $1 --output ./malletstuff/input-tokens.mallet --keep-sequence --remove-stopwords
./mallet-2.0.7/bin/mallet train-topics --input ./malletstuff/input-tokens.mallet --num-topics $2 --optimize-interval 20 --output-doc-topics ./malletstuff/alldocs.txt --random-seed 1 --inferencer-filename ./malletstuff/topic-inferencer.inf

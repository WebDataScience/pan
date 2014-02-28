#!/bin/bash

#export _JAVA_OPTIONS='-Xmx6g'
echo 'Infering topics for testing'
./mallet-2.0.7/bin/mallet import-dir --input $1 --remove-stopwords --keep-sequence --output ./malletstuff/testingtokens.mallet
./mallet-2.0.7/bin/mallet infer-topics --input ./malletstuff/testingtokens.mallet --random-seed 1 --output-doc-topics $2 --inferencer ./malletstuff/topic-inferencer.inf

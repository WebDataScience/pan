#!/bin/bash

export _JAVA_OPTIONS='-Xmx6g'
echo 'Infering topics' 
./mallet-2.0.7/bin/mallet import-file --input $1 --remove-stopwords --keep-sequence --output ./malletstuff/labeltokens.mallet
./mallet-2.0.7/bin/mallet infer-topics --input ./malletstuff/labeltokens.mallet --random-seed 1 --output-doc-topics $2 --inferencer ./malletstuff/topic-inferencer.inf

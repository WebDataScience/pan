#!/bin/bash

#export _JAVA_OPTIONS='-Xmx3g'
./mallet-2.0.7/bin/mallet import-dir --input $1 --output ./malletstuff/input-tokens.mallet --keep-sequence --remove-stopwords
./mallet-2.0.7/bin/mallet infer-topics --input ./malletstuff/input-tokens.mallet --random-seed 1 --output-doc-topics $2 --inferencer $3
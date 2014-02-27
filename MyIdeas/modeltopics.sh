#!/bin/bash

#export _JAVA_OPTIONS='-Xmx6g'
/home/jamarq/Desktop/mallet-2.0.7/bin/mallet import-dir --input $1 --output input-tokens.mallet --keep-sequence --remove-stopwords
/home/jamarq/Desktop/mallet-2.0.7/bin/mallet train-topics --input input-tokens.mallet --num-topics $2 --optimize-interval 20 --output-doc-topics input-composition.txt --random-seed 1 --inferencer-filename topic-inferencer.inf
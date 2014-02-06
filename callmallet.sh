#!/bin/bash

./mallet-2.0.7/bin/mallet import-dir --input /Users/the_james_marq/PAN/Data/subset_training1 --output ./outputs/tokens.mallet --keep-sequence --remove-stopwords
./mallet-2.0.7/bin/mallet train-topics  --input ./outputs/tokens.mallet  --num-topics 20 --optimize-interval 20 --output-state ./outputs/topic-state.gz  --output-topic-keys ./outputs/keys.txt --output-doc-topics ./outputs/composition.txt

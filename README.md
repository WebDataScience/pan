pan - author profiling
===

Currently only implements topic based prediction
---

Predicts age and gender (combined) of a author based on textual data.

To run, navigate to project directory, and run

> $ python pymallet.py

This will generate topic model formatted into a usable format to be used in prediction

To generate cross validation data, call

> $ python CrossValidationMaker.py

This will create a "folds" subdirectory where your original model was and place in it k folds. The first 90% of each fold to be used for training, the last 10% for testing.

To test the model's use in prediction, we have included a test script. The script will perform SVM classification with a linear kernel. To run the classifier, call

> $ python SVMTest.py

This will iterate through all of the cross validation folds and output the accuracy of predictions
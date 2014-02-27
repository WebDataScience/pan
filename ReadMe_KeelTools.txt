1. to convert form csv to keel format

the csv files to be named as topicdiv-10-1tra.csv and topicdiv-10-1tst.csv
dataset dummy location:
C:\Users\Gayathri\Documents\Acads\4 Winter 14\pan\topicdiv\4_svm\4_svm\datasets\topicdiv

syntax:
(pass only 1 argument which are apended with $)
execute
java -jar JarConvertCSVToKeel.jar "train_data_location$dataset_dummyexperiment$test_Data_location$dataset_dummyexperiment

example:
java -jar JarConvertCSVToKeel.jar "C:\Users\Gayathri\Documents\Acads\4 Winter 14\pan\topicdiv\test_convert_csv_to_keel\topicdiv-10-1tra.csv$C:\Users\Gayathri\Documents\Acads\4 Winter 14\pan\topicdiv\4_svm\4_svm\datasets\topicdiv$C:\Users\Gayathri\Documents\Acads\4 Winter 14\pan\topicdiv\test_convert_csv_to_keel\topicdiv-10-1tst.csv$C:\Users\Gayathri\Documents\Acads\4 Winter 14\pan\topicdiv\4_svm\4_svm\datasets\topicdiv"

2. no need to change config file, since the dataset is placed in the correct path of the experiment.

3. to run experiment
goto directory:
C:\Users\Gayathri\Documents\Acads\4 Winter 14\pan\topicdiv\4_svm\4_svm\scripts

execute
java -jar RunKeel.jar

4. to generate xml
goto C:\Users\Gayathri\Documents\Acads\4 Winter 14\pan\topicdiv

syntax:
(pass only 1 argument which are apended with $)
execute
java -jar JarConvertCSVToKeel.jar docid_csv_location$resultsofexpt_location$language(en or es)$type$location_xmls_to_be_saved

example:
jar -jar JarGenerateXML.jar "C:\Users\Gayathri\Documents\Acads\4 Winter 14\pan\topicdiv\test_convert_csv_to_keel\authorid.csv$C:\Users\Gayathri\Documents\Acads\4 Winter 14\pan\topicdiv\4_svm\4_svm\results\C_SVM-C.topicdiv\result0s0.tst$en$social$C:\Users\Gayathri\Documents\Acads\4 Winter 14\pan\topicdiv\en_social"
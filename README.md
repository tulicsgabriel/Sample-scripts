# Sample-scripts
Examples of short scripts that I used for work

FilterFeaturesFromTxt.py - The script is used for filtering out features not needed for futher work. It loops through an input directory, checks all txt files. If the column name in the txt file contains an MFCC feature it copies its data to a separate file. 
Writes each file to an output directory.

Txt files contain data as follows (f ->feature name):
     f1   f2   f3
0    10   5    5
1     9   3    4
2     8   7    0

confusion_matrix_3x3.py - Calculates metrics from 3x3 confusion matrices. Defined metrics: accuracy, error rate, recall (sensitivity), precision, specificity, F_score.

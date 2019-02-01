# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 17:13:59 2019

@author: miklos
"""

import numpy as np
import pandas as pd

def recall(label, confusion_matrix):
    col = confusion_matrix[:, label]
    return (confusion_matrix[label, label] / col.sum())*100
    
def precision(label, confusion_matrix):
    row = confusion_matrix[label, :]
    return (confusion_matrix[label, label] / row.sum())*100

def sensitivity(label, confusion_matrix):
    # Sensitivity, hit rate, recall, or true positive rate -> TPR = TP/(TP+FN)
    col = confusion_matrix[:, label]
    return (confusion_matrix[label, label] / col.sum())*100

def specificity(label, confusion_matrix):
# Specificity or true negative rate -> TNR = TN/(TN+FP)   
    if label == 0:
        numerator = confusion_matrix[1,1] + confusion_matrix [1,2] + confusion_matrix [2,1] + confusion_matrix[2,2]
        denominator = numerator + confusion_matrix[0,1] + confusion_matrix[0,2]
        return (numerator / denominator)*100     
    if label == 1:
        numerator = confusion_matrix[0,0] + confusion_matrix [2,0] + confusion_matrix [0,2] + confusion_matrix[2,2]
        denominator = numerator + confusion_matrix[1,0] + confusion_matrix[1,2]
        return (numerator / denominator)*100    
    if label == 2:
        numerator = confusion_matrix[0,0] + confusion_matrix [0,1] + confusion_matrix [1,0] + confusion_matrix[1,1]
        denominator = numerator + confusion_matrix[2,0] + confusion_matrix[2,1]
        return (numerator / denominator)*100     

def accuracy(confusion_matrix):
    numerator = confusion_matrix[0,0] + confusion_matrix[1,1] + confusion_matrix[2,2]
    col1 = confusion_matrix[:, 0]
    col2 = confusion_matrix[:, 1]
    col3 = confusion_matrix[:, 2]
    denominator = col1.sum() + col2.sum() + col3.sum()
    return  (numerator / denominator)*100

def error_rate(confusion_matrix):
    numerator = confusion_matrix[0,0] + confusion_matrix[1,1] + confusion_matrix[2,2]
    col1 = confusion_matrix[:, 0]
    col2 = confusion_matrix[:, 1]
    col3 = confusion_matrix[:, 2]
    denominator = col1.sum() + col2.sum() + col3.sum()
    return (1 - (numerator / denominator))*100

def F_score(label, confusion_matrix):
    return 2 * ((precision(label, cm)*recall(label, cm))/(precision(label, cm)+recall(label, cm)))

# =============================================================================
#  Used input here
# =============================================================================

label_names = ["Healthy", "Func", "Struct"]

cm = np.array(
[[7, 0, 4],
 [2, 19, 10],
 [3, 8, 4]])
    
label_names_pred = []
label_names_true = []

for i in range(0,3):
    label_names_pred.append("pred_" + label_names[i])
    label_names_true.append("true_" + label_names[i])

dataDF = pd.DataFrame(cm, label_names_pred, label_names_true)
print(dataDF)
print("\n")

# =============================================================================
#   Leave the rest to do it for you!
#
#   First we print out the sensitivity and specificity  
# =============================================================================

measures = ["Sensitivity", "Specificity"]
"""
print("Label \t Precision \t Recall")
for label in range(0,3):
    print(f"{label_names[label]} \t {precision(label, cm):6.4f} \t {recall(label, cm):6.4f}")

print("\n")
"""
result_array = np.empty((0, 2))
#print("Label \t Sensitivity \t Specificity")
for label in range(0,3):
    JustATempArray = np.array([sensitivity(label, cm), specificity(label, cm)])
    result_array = np.vstack((result_array, JustATempArray))    
    #print(f"{label_names[label]} \t {sensitivity(label, cm):6.4f} \t {specificity(label, cm):6.4f}")

dataDF2 = pd.DataFrame(result_array, label_names, measures)
print(dataDF2)
print("\n")

# =============================================================================
# Print out the accuracy and the error rate
# =============================================================================

print(f"Accuracy: {accuracy(cm):6.4f}%")
print(f"Error rate: {error_rate(cm):6.4f}%")
print("\n")

# =============================================================================
# Here's the F-score
# The F-score is the harmonic mean of precision and recall
# =============================================================================

fscore_array = np.empty((0, 1))

for label in range(0,3):
    Fscore =  F_score(label, cm)
    fscore_array = np.concatenate((fscore_array, np.array([[Fscore]])), axis=0)

dataDF3 = pd.DataFrame(fscore_array, label_names, ["F-score"])
print(dataDF3)
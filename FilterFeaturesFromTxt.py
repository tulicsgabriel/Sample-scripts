# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:15:30 2018

@author: miklos

Loop through a directory, check txt files, if the column name contains an MFCC feature, copy its to a separate file. 
Write each file to output directory  
"""

# Importing the libraries
import numpy as np
import glob, os
import pandas as pd

# Set relative paths
path = os.path.dirname(__file__)
pathIn = os.path.join(path, 'Input')
pathOut =os.path.join(path, 'Output')

# If Output directory doesn't exist, create it
if not os.path.exists(pathOut):
    os.makedirs(pathOut)

#pathIn =   r"e:\Shared\Miklos\_Python-Projects\Filter_Features\Input"
#pathOut=   r"e:\Shared\Miklos\_Python-Projects\Filter_Features\Output"

os.chdir(pathIn)
for file in glob.glob("*.txt"):
    with open(file) as f:
        dataset = pd.read_csv(f, sep='\t')
        dataset2 = dataset[[x for x in dataset.columns if "mfcc" in x]]  
        base = os.path.basename(file)
        base = os.path.splitext(base)[0]
        base = base.replace('wav', '')
        os.chdir(pathOut)
        np.savetxt(base + "bas", dataset2.values, delimiter ='\t', fmt  = '%.15g')
        os.chdir(pathIn)




    


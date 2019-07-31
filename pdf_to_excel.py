#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 19:34:50 2019

@author: enricotorriero
"""

from tabula import read_pdf
import pandas as pd
import numpy as np

# importing pdf file
dataset = read_pdf("ListaGuias.pdf", pages = "all", multiple_tables = True)

# creating a dataframe with all information
df = pd.DataFrame()
for i in range(118):
    x = dataset[i]
    df = df.append(x)
    
# exporting to excel file 
df.to_excel("output.xlsx")
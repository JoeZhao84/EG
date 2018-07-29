# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 21:53:13 2018

@author: LinusZhao
"""

import os
os.chdir('C:\Work\workspaces\Spyder')
#os.chdir('D:\Betsson_20180122\RnD\RejectionSampling')
import pandas as pd
import numpy as np
import math

df = pd.read_csv('Titanic.csv')

df.head(5)

df.dtypes

df.groupby(['Pclass', 'Sex', 'Embarked']).size()

#so the biggest difference is male/S/3: 265 and female/s/3: 88
#ratio = 88 / 265    #0.33..

Pclass_list = df.Pclass.unique()
Embarked_list = df.Embarked.unique()
Embarked_list = Embarked_list[~pd.isnull(Embarked_list)]
#Sex_list = df.Sex.unique()

def get_ratio(df):
    ratios = []
    for a in Pclass_list:
        for b in Embarked_list:
            male_count = df[(df['Pclass'] == a) & (df['Embarked'] == b) & (df['Sex'] == 'male')]['Sex'].count()
            female_count = df[(df['Pclass'] == a) & (df['Embarked'] == b) & (df['Sex'] == 'female')]['Sex'].count()
            ratio = female_count / male_count
            ratios.append(ratio)
            min_ratio = min(ratios)
    return min_ratio

ratio =  get_ratio(df)           
                
def get_RejSample(df):
    newDF = pd.DataFrame() 
    for a in Pclass_list:
        for b in Embarked_list:
            male_count = df[(df['Pclass'] == a) & (df['Embarked'] == b) & (df['Sex'] == 'male')]['Sex'].count()
            female_count_e = int(round(male_count * ratio))
            acc_sample = df[(df['Pclass'] == a) & (df['Embarked'] == b) & (df['Sex'] == 'female')].sample(n=female_count_e,replace=True)
            newDF = newDF.append(acc_sample, ignore_index=True)   
    return newDF
    
#test
sample = get_RejSample(df)
#newDF[(newDF['Pclass'] == 1) & (newDF['Embarked'] == 'C') & (newDF['Sex'] == 'female')].count()
sample[(sample['Pclass'] == 1) & (sample['Embarked'] == 'S') & (sample['Sex'] == 'female')].count()
   
    
    
    
   
male_count = df[(df['Pclass'] == 1) & (df['Embarked'] == 'C') & (df['Sex'] == 'male')]['Sex'].count()
female_count_e = int(round(male_count * ratio))

acc_sample = df[(df['Pclass'] == 1) & (df['Embarked'] == 'C') & (df['Sex'] == 'female')].sample(n=female_count_e,replace=True)

newDF = pd.DataFrame() 
newDF = newDF.append(acc_sample, ignore_index=True)    

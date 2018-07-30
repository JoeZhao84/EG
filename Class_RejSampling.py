# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 16:30:38 2018

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

class RejSampling(object):
    """
    """
    def __init__(self):
        self.variables = []
        
    def get_variables(self,variables):
        self.variables = variables
        
    def get_list(self,df):
        n_var = len(self.variables)
        unique_list = [None] * len(self.variables)
        for i in range(n_var):
            t = df[self.variables[i]].unique()
            unique_list[i] = t[~pd.isnull(t)]
        return unique_list
           
    def get_ratio(self,df,control_variable,control,test):
        ratios = []
        import itertools
        unique_pair_list = []
        for element in itertools.product(*unique_list):
            unique_pair_list.append(element)
            
        for i in unique_pair_list:
            temp_df = df[(df[self.variables[0]] == i[0])]
            j = 1
            while j < len(self.variables):
                temp_df = temp_df[(temp_df[self.variables[j]] == i[j])]
                j = j + 1
            male_count = temp_df[temp_df[control_variable] == control][control_variable].count()
            female_count = temp_df[temp_df[control_variable] == test][control_variable].count()
            ratio = female_count / male_count
            ratios.append(ratio)
            nonnan_ratios = [x for x in ratios if str(x) != 'nan']
            nonnan_nonzero_ratios = [x for x in nonnan_ratios if x != 0.0]
            min_ratio = np.min(nonnan_nonzero_ratios)
            #print(nonnan_ratios)
        return min_ratio
    
    
#        for i in unique_pair_list:
#            male_count = df[(df[self.variables[0]] == i[0]) & (df[self.variables[1]] == i[1]) & (df['Sex'] == 'male')]['Sex'].count()
#            female_count = df[(df[self.variables[0]] == i[0]) & (df[self.variables[1]] == i[1]) & (df['Sex'] == 'female')]['Sex'].count()
#            ratio = female_count / male_count
#            ratios.append(ratio)
#            min_ratio = min(ratios)
#        return min_ratio
    
    def get_sample(self,df,control_variable,control,test):
        newDF = pd.DataFrame()
        import itertools
        unique_pair_list = []
        for element in itertools.product(*unique_list):
            unique_pair_list.append(element)
            
        for i in unique_pair_list:
            temp_df = df[(df[self.variables[0]] == i[0])]
            j = 1
            while j < len(self.variables):
                temp_df = temp_df[(temp_df[self.variables[j]] == i[j])]
                j = j + 1
            male_count = temp_df[temp_df[control_variable] == control][control_variable].count()
            female_count_e = int(round(male_count * ratio))
            if female_count_e == 0:
                pass  
            elif temp_df[temp_df[control_variable] == test][control_variable].count() == 0:
                pass
            else:
                acc_sample =  temp_df[temp_df[control_variable] == test].sample(n=female_count_e,replace=True)
            #print(acc_sample)
                newDF = newDF.append(acc_sample, ignore_index=True)
        return newDF

#unique_list = get_data(df,['Pclass', 'Embarked'])
################ usage ###################
sample = RejSampling()  
variables = sample.get_variables(['Pclass', 'Embarked'])  
unique_list = sample.get_list(df)
ratio = sample.get_ratio(df,'Sex','male','female')
s = sample.get_sample(df,'Sex','male','female')

##########################################


t[1]
t = []
a=[1,2,3]
b=[4,5,6]
c=[7,8,9]


for i in tt:
    temp_df = df[(df[self.variables[0]] == i[0])
    for j in range(len(self.variables)-1):
        temp_df = temp_df[(temp_df[self.variables[j+1]] == i[j+1])
        #print(j)
        #male_count = temp_df[['Sex'] == 'male')]['Sex'].count()
        #female_count = temp_df[['Sex'] == 'female')]['Sex'].count()
        #ratio = female_count / male_count
        #ratios.append(ratio)
        #min_ratio = min(ratios)
return temp_df    
  
    

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 23:23:19 2018

@author: LinusZhao
"""

import numpy as np

class ExponentialGradient:
    def test_case_1(self):
        data_set_1 = np.array([
            [[0.343,0.2], [0.535,0.1], [0.412,0.1], [1.634,0.1], [0.237,0.1]],
            [[0.246,0.246], [0.432,0.1], [0.675,0.1], [1.293,0.1], [0.147,0.1]]
        ])
        self.weighted_vote_method(data_set_1)

    def weighted_vote_method(self, data_set, learning_rate=0.3):
        if len(data_set) <= 0:
            raise ValueError("Data set length error.")

        weight_result = []

        # Initialize weight.
        current_weight = [1. / len(data_set[:,0]) for i in range(len(data_set[:,0]))]
        # Import data by column
        for i in range(len(data_set[0])):
            print("Current weight=\t\t" + str(current_weight))
            current_weight = self.exponentiated_gradient(data_set[:,i], current_weight, learning_rate)
            weight_result.append(current_weight)
            print("===================")

    def exponentiated_gradient(self, data_set, previous_weight, learning_rate):
        if len(data_set) <= 0:
            raise ValueError("Data set length error.")
        if len(data_set) != len(previous_weight):
            raise ValueError("Arguments length not equal.")

        print("Data set =\t\t" + str(data_set))

        result = []
        #all_weighted_value = np.sum([previous_weight[i] * data_set[i] for i in range(len(data_set))])
        #numerator = np.sum([previous_weight[i] * np.exp((learning_rate * data_set[i]) / all_weighted_value) for i in range(len(data_set))])
        #print("Numerator=\t\t\t" + str(numerator))
        
        g = []
        for i in range(len(data_set)):
            if data_set[i][1] == data_set[i][0]:
                g.append(1)
            else:
                g.append(0)
        print(g)
        
        all_weighted_value = np.sum([previous_weight[i] * data_set[0][i] for i in range(len(data_set))])   
        numerator = np.sum([previous_weight[i] * np.exp((learning_rate * g[i]) / all_weighted_value) for i in range(len(data_set))])        
        print("Numerator=\t\t\t" + str(numerator))
        
        for i in range(len(data_set)):    
            fractions = previous_weight[i] * np.exp((learning_rate * g[i]) / all_weighted_value)
            result.append(fractions / numerator)
          
        print("Result=\t\t\t\t" + str(result))
        return result

a = ExponentialGradient()
a.test_case_1()



data_set_1 = np.array([
            [[0.343,0.1], [0.535,0.1], [0.412,0.1], [1.634,0.1], [0.237,0.1]],
            [[0.246,0.1], [0.432,0.1], [0.675,0.1], [1.293,0.1], [0.147,0.1]]
        ])
    
data_set_2 = np.array([
            [0.343, 0.535, 0.412, -1.634, 0.237],
            [0.246, 0.432, -0.675, 1.293, 0.147]
        ])

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:30:27 2020

@author: Nihar Kanungo
"""


import math

__all__ = ['sigmoid']
def sigmoid(x):
    '''
    Calculates the Sigmoid  of the given value 
    FInd out the derivative of the Sigmoid of the given value
    '''
    print(f'the value of sigmoid for given input is {1 / (1 + math.exp(-x))}')
    return 1 / (1 + math.exp(-x))


def sigmoid_der(x):
    print(f'the value of derivative for sigmoid for given input is {sigmoid(x)*(1-sigmoid(x))}')
    return sigmoid(x)*(1-sigmoid(x))

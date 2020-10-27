"""
Created on Tue Oct 27 16:30:27 2020

@author: Nihar Kanungo
"""


import math
__all__ = ['exponential']
def exponential(x):
    '''
    Calculates the exponential of the given value 
    FInd out the derivative of the exponential of the given value 
    '''
    print(f'the value of exponential for the input is {math.exp(x)}')
    return math.exp(x)

def derivative_exp(x):
    print(f'the value of derivative of  exponential for the input is {math.exp(x)}')
    return math.exp(x)

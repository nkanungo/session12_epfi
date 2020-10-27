"""
Created on Tue Oct 27 16:30:27 2020

@author: Nihar Kanungo
"""

import math
__all__ = ['cos']
def cos(x):
    '''
    Calculates the cos of the given value 
    FInd out the derivative of the cos of the given value 

    '''
    print(f'the value of cos of given input is: {math.cos(x)}')
    return math.cos(x)
def der_cos(x):
    print(f'the value of the derivative of cos for given input is : {-(math.sin(x))}')
    return -(math.sin(x))

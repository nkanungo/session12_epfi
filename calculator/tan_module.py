"""
Created on Tue Oct 27 16:30:27 2020

@author: Nihar Kanungo
"""


import math
__all__ = ['tan']

def tan(x):
    '''
    Calculates the tan of the given value 
    FInd out the derivative of the tan of the given value 
    '''
    print(f'the value for the tanx of given input is : {math.tan(x)}')
    return math.tan(x)
def der_tan(x):
    print(f'the derivative value for the tanx of given input is : {1/((math.cos(x))**2)}')
    return 1/((math.cos(x))**2)

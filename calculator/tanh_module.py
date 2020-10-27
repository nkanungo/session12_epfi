
"""
Created on Tue Oct 27 16:30:27 2020

@author: Nihar Kanungo
"""



import math
__all__ = ['tanh']
def tanh(x):
    print(f'the value for the tanhx of given input is : {math.tanh(x)}')
    return math.tanh(x)


def der_tanh(x):
    print(f'the value for the derivative of tanhx of given input is : {1/(math.cosh(2*x))}')
    return 1/(math.cosh(2*x))

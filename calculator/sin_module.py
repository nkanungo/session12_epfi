"""
Created on Tue Oct 27 16:30:27 2020

@author: Nihar Kanungo
"""

import math
__all__ = ['sin']
def sin(x):
    print(f'the value of sin for given input is :{math.sin(x)}')
    return math.sin(x)
def der_sin(x):
    print(f'the value of derivative of sin given : {math.cos(x)} ')
    return math.cos(x)

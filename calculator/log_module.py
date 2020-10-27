"""
Created on Tue Oct 27 16:30:27 2020

@author: Nihar Kanungo
"""


import math

__all__ = ['log']
def log(x,base):
    print(f'the return value is {math.log(x,base)}')
    return math.log(x,base)

def derivative_log(x,base):
    print(f'the return value is {1/(x * math.log(base,math.e))}')
    return 1/(x * math.log(base,math.e))

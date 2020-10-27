"""
Created on Tue Oct 27 16:30:27 2020

@author: Nihar Kanungo
"""


__all__ = ['relu']

def relu(x):
    print(f'the value of relu for given input is { x if x> 0 else 0}')
    return x if x> 0 else 0

def derivative_relu(x):
    print(f'the value of relu for given input is { 1 if x>0 else 0}')
    return 1 if x>0 else 0

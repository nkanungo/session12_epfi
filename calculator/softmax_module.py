"""
Created on Tue Oct 27 16:30:27 2020

@author: Nihar Kanungo
"""


import numpy as np
__all__ = ['softmax']


def softmax(x):
    '''
    \sigma(z_{i})=\frac{e^{z_{i}}} {\sum_{j=1}^K e^{z_{j}}}
    '''
    if len(x) <2:
        raise ValueError (' Softmax works for more than two values')
    """ applies softmax to an input x"""
    e_x = np.exp(x - np.max(x))
    print(f'the softmax for the given input is :{e_x / e_x.sum()}')
    return e_x / e_x.sum()

def softmax_derivative(x):
    '''
    \frac{\delta{S_{i}}}{\delta{x_{j}}}=\frac{\delta{\frac{e^{x_{i}}} {\sum_{k=1}^N e^{x_{k}}}}}{\delta{x_{j}}}
      Following Bendersky’s derivation, we need to use the quotient rule for derivatives:

    \text{If }f(x)=\frac{g(x)}{h(x)} \text{ then:}

     f'(x)=\frac{g'(x)h(x)-h'(x)g(x)}{[h(x)]^{2}}

     From the Softmax function:

     \begin{array}{rcl} g_{i} & = & e^{x_{i}}\\ h_{i} & = & \sum_{k=1}^N e^{x_{k}} \end{array}

     \frac{\delta{g_{i}}}{\delta{x_{j}}} = \left \{ \begin{aligned} &e^{x_{j}}, && \text{if}\ i=j \\ &0, && \text{otherwise} \end{aligned} \right.
      and

      \frac{\delta{h_{i}}}{\delta{x_{j}}}=\frac{\delta(e^{x_{1}}+e^{x_{2}}+...+e^{x_{N}})}{\delta{x_{j}}}=e^{x_{j}}

       Now we have to evalutate the quotient rule for the two seperate cases where i=j and where i\neq{j}:

       Starting with i=j:

       \frac{\delta{\frac{e^{x_{i}}} {\sum_{k=1}^N e^{x_{k}}}}}{\delta{x_{j}}}=\frac{e^{x_{j}}\sum_{k=1}^N e^{x_{k}}-e^{x_{j}}e^{x_{i}}}{\left[\sum_{k=1}^N e^{x_{k}}\right]^{2}}

        Now we’ll just simplify this a bit:

        \begin{array}{rcl} \frac{\delta{\frac{e^{x_{i}}} {\sum_{k=1}^N e^{x_{k}}}}}{\delta{x_{j}}} & = & \frac{e^{x_{j}}\left(\sum_{k=1}^N e^{x_{k}}-e^{x_{i}}\right)}{\left[\sum_{k=1}^N e^{x_{k}}\right]^{2}}\\ &=&\frac{e^{x_{j}}}{\sum_{k=1}^N e^{x_{k}}} \dot{}\frac{\sum_{k=1}^N e^{x_{k}}-e^{x_{i}}}{\sum_{k=1}^N e^{x_{k}}}\\ &=&\frac{e^{x_{j}}}{\sum_{k=1}^N e^{x_{k}}} \left(\frac{\sum_{k=1}^N e^{x_{k}}}{\sum_{k=1}^N e^{x_{k}}}-\frac{e^{x_{i}}}{\sum_{k=1}^N e^{x_{k}}}\right)\\ &=&\frac{e^{x_{j}}}{\sum_{k=1}^N e^{x_{k}}} \left(1-\frac{e^{x_{i}}}{\sum_{k=1}^N e^{x_{k}}}\right)\\ &=&\sigma(x_{j})(1-\sigma(x_{i})) \end{array}

         For the case where i\neq j:

         \begin{array}{rcl} \frac{\delta{\frac{e^{x_{i}}} {\sum_{k=1}^N e^{x_{k}}}}}{\delta{x_{j}}}&=&\frac{0-e^{x_{j}}e^{x_{i}}}{\left[\sum_{k=1}^N e^{x_{k}}\right]^{2}}\\ &=&0-\frac{e^{x_{j}}}{\sum_{k=1}^N e^{x_{k}}}\dot{}\frac{e^{x_{i}}}{\sum_{k=1}^N e^{x_{k}}}\\ &=&0-\sigma(x_{j})\sigma(x_{i}) \end{array}

    '''
    S=softmax(x)
    S_vector = S.reshape(S.shape[0],1)
    S_matrix = np.tile(S_vector,S.shape[0])
    #print(S_matrix, '\n')
    output = np.diag(S)[0] - (S_matrix * np.transpose(S_matrix))[0]
    print(f'the derivative of softmax for given input is= {output}')
    return np.diag(S)[0] - (S_matrix * np.transpose(S_matrix))[0]
    #S_vector = S.reshape(S.shape[0],1)
    #S_matrix = np.tile(S_vector,S.shape[0])
    #print(f'the derivative of softmax for given input is : {np.diag(S)[0] - (S_matrix * np.transpose(S_matrix))[0]}')
    #return np.diag(S)[0] - (S_matrix * np.transpose(S_matrix))[0]
    #return np.diag(S)[0] - (S_matrix * np.transpose(S_matrix))[0]
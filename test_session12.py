# -*- coding: utf-8 -*-
import pytest
import os
import inspect
import re
import calculator
import numpy as np

from pathlib import Path
path = Path('./calculator')
README_CONTENT_CHECK_FOR = [

]

CHECK_FOR_THINGS_NOT_ALLOWED = [
    
]

def test_readme_exists():
    print('==',os.path)
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 250, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 0
'''
def test_indentations():
   
    modules = inspect.getmembers(calculator, inspect.ismodule)
    for module in modules:
        lines = inspect.getsource(module[1])
        print(module[1])
        spaces = re.findall('\n +.', lines)
        line_no =1
        for space in spaces:
            line_no +=1
            print('=====', line_no, space)
            assert re.search('[a-zA-Z#@=1234\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
            assert len(re.sub(r'[a-zA-Z#@=1234\n\"\']', '', space)) % 4 == 0, \
            "Your code intentation does not follow PEP8 guidelines"
 '''       

def test_function_name_had_cap_letter():
    files = [file for file in path.iterdir() if '.py' in file.suffix ]
    for file in files:
        functions = inspect.getmembers(file.name, inspect.isfunction)
        for function in functions:
            assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_sin_import():
    sin_zero = calculator.sin(0)  
    assert sin_zero == 0.0,"sin function in calculor has wrong implementation"
    
def test_der_sin_import():
    der_sin_zero = calculator.sin_module.der_sin(0)
    assert (der_sin_zero == 1),"derivative of sin function has wrong implementation"
    
def test_cos_import():
    cos_zero =calculator.cos(0)  
    assert cos_zero == 1,"cos function in calculor has wrong implementation"
    
def test_der_sin_import():
    der_cos_zero = calculator.cos_module.der_cos(0)
    assert (der_cos_zero == 0),"derivative of cos function has wrong implementation"
    
def test_sigmoid_import():
    sigmoid_zero =calculator.sigmoid(0)  
    assert sigmoid_zero == 0.5,"sigmoid function in calculor has wrong implementation"
    
def test_der_sigmoid_import():
    der_sigmoid_zero = calculator.sigmoid_module.sigmoid_der(0)
    assert (der_sigmoid_zero == 0.25),"derivative of sigmoid function has wrong implementation"
    
def test_softmax_import():
    softmax_output =calculator.softmax([1,5])  
    assert np.allclose(softmax_output,np.array([0.01798621, 0.98201379])),"softmax function in calculor has wrong implementation"

def test_der_softmax_import():
    der_softmax_output = calculator.softmax_module.softmax_derivative(np.array([1,5])) 
    assert np.allclose(der_softmax_output, np.array([0.01766271, -0.01766271])),"derivative of softmax function has wrong implementation"
   
def test_tan_import():
    tan_output =calculator.tan(22/28)  
    assert round(tan_output)==1,"tan function in calculor has wrong implementation"
    
def test_der_tan_import():
    der_tan_zero = calculator.tan_module.der_tan(22/28)
    assert (round(der_tan_zero) == 2),"derivative of tan function has wrong implementation"
    
def test_tanh_import():
    tanh_output =calculator.tanh(22/28)  
    assert round(tanh_output,2)==0.66,"tanh function in calculor has wrong implementation"
 
def test_der_tan_import():
    der_tanh = calculator.tanh_module.der_tanh(22/28)
    assert (round(der_tanh,2) == 0.4),"derivative of tanh function has wrong implementation"
def test_relu_import():
    relu_output = calculator.relu(5)
    assert (relu_output == 5),"derivative of relu function has wrong implementation"

def test_der_relu_import():
    der_relu = calculator.relu_module.derivative_relu(-1)
    assert (der_relu == 0),"derivative of relu function has wrong implementation"

def test_exp_import():
    exp1 = calculator.exponential(2)
    assert (exp1 == 7.38905609893065),"derivative of relu function has wrong implementation"

def test_der_exp_import():
    der_exp = calculator.exponential__module.derivative_exp(2)
    assert (der_exp == 7.38905609893065),"derivative of relu function has wrong implementation"

def test_log_import():
    log_val = calculator.log(10,4)
    assert (log_val == 1.6609640474436813),"derivative of relu function has wrong implementation"

def test_der_log_import():
    der_log = calculator.log_module.derivative_log(10,4)
    assert (der_log == 0.07213475204444816),"derivative of log function has wrong implementation"
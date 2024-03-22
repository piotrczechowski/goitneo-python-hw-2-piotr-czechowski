from main import *

def my_function(x, y):
    return x / y  

@input_error
def test_input_error_decorator():
    result = my_function(10, "abc")  
    return result



result = test_input_error_decorator()

def my_function(lst, index):
    return lst[index]  

@input_error
def test_input_error_decorator():
    result = my_function([1, 2, 3], 10)  
    return result

result = test_input_error_decorator()
print(result)  


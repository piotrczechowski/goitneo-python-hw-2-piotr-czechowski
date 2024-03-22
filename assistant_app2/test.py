from main import *

def my_function(x, y):
    return x / y  

@input_error
def test_input_error_decorator():
    result = my_function(10, "abc")  
    return result



result = test_input_error_decorator()

def my_function(lst, index):
    return lst[index]  # This will raise an IndexError if the index is out of range

@input_error
def test_input_error_decorator():
    result = my_function([1, 2, 3], 10)  # This will intentionally raise an IndexError
    return result

# Execute the test function
result = test_input_error_decorator()
print(result)  


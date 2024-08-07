import numpy as np
import pandas as pd
list1 = [1, 2, 3, 4, 5]
array1 = np.array([1, 2, 3, 4, 5])
list2 = [6, 7, 8, 9, 10]
array2 = np.array([6, 7, 8, 9, 10])
list1_type = type(list1)
array1_type = type(array1)
series1 = pd.Series(list1)
series2 = pd.Series(list2)
mult_result = array1 * array2  
div_result = array1 / array2    
pow_result = array1 ** 2 


text_output = f'Addition of Two: {array1 + array2}'




math_functions_output = {
    'sin': np.sin(array1),
    'log': np.log(array1),
    'log2': np.log2(array1),
    'exp': np.exp(array1)
}



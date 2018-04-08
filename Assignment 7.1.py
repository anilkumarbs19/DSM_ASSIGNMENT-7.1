
# coding: utf-8

# In[42]:


import numpy as np

def moving_average(input_array, k=3) :
    input_array_shape = input_array.shape[0]
    out_array_moving_avg = np.zeros(input_array_shape - k + 1)
    for i in range(k, input_array_shape + 1):
        out_array_moving_avg[i-k] = input_array[i-k:i].mean()
    
    return out_array_moving_avg   
### O/P ###
a = np.array([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150])
size = 3
moving_average_arr = moving_average(a, size)

print("The input sequence is =", a, "\n")
print("The moving average of the sequence with the size", size, "is =\n", moving_average_arr, "\n")
print("The moving average sequence has", moving_average_arr.shape[0], "values.")


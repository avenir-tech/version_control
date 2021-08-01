print('Hello World!')

def square_and_sum(lst):
    import numpy as np
    lst = np.array(lst)
    return np.square(lst).sum()

lst = [1, 2, 3]

print(f'Testing with list: {lst}, and the result is: {square_and_sum(lst)}.')

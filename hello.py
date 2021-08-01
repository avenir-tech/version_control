print('Hello World!')

def square_and_sum(lst):
    return sum([i * i for i in lst])

lst = [1, 2, 3]

print(f'Testing with list: {lst}, and the result is: {square_and_sum(lst)}.')

print('Hello World!')

def square_and_sum(lst):
    sum = 0
    for i in lst:
        sum += i * i
    return sum

lst = [1, 2, 3]

print(f'Testing with list: {lst}, and the result is: {square_and_sum(lst)}.')

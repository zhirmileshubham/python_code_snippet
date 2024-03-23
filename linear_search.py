'''
linear search algorithm
'''

def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [1,2,4,6,8,9]
x = 14
result = linear_search(arr,x)

if result != -1:
    print(f'Element present at index {result}')
else:
    print('Element is not present in array')
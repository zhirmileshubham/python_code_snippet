'''
For the given list add integers present in the list and return new list
[7234, 2211, 8764] --> [7777, 2222, 8888] --> [28, 8, 32]
'''

def list_ops(arr):
    for ind, i in enumerate(arr):
        a = max([int(a) for a in list(str(i))])
        arr[ind] = sum([int(b) for b in list(str(a)*len(str(i)))])

    return arr

arr = [7234, 2211, 8764]

result = list_ops(arr)
print('Result of list operation is :',result)

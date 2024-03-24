'''
Insert and Delete elements in given index
'''




def add_ele(ind, val):
    l1 = [1,2,3,4]
    return l1[:ind]+ [val] + l1[ind:]

result_add = add_ele(1, 3)

def del_ele(ind):
    l2 = [4,5,6]
    return l2[:ind] + l2[ind+1:]

result_del = del_ele(0)

print(result_add)
print(result_del)
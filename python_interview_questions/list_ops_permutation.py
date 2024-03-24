'''
Find all possible permutaion for given to string
s1 = 'abcabaabccbaabc'
s2 = 'abc'
'''

def string_permutation(s1,s2):
    for ind in range(0, len(s1)-2):
        count = 0
        list_t = []
        string_t = ''
        if set((s1[ind], s1[ind+1], s1[ind+2])) == set(s2):
            list_t.append(s1[ind] + s1[ind+1] + s1[ind+2])
            count += 1
    return list_t, count

s1 = 'abcabaabccbaabc'
s2 = 'abc'

list_r, count_r = string_permutation(s1, s2)

print("Resultant list", list_r)
print("resultant count", count_r)



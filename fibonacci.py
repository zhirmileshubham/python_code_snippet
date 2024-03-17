'''
This code calculates the fibonacci for number range
'''

def fibno(n):
    if n <= 1:
        return n
    else:
        return fibno(n-1) + fibno(n-2)

terms = int(input("Enter number of inputs: "))
print("fibonacci series")

for i in range(terms):
    print(fibno(i))
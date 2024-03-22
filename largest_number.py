# Find largest number

'''
This code takes 3 numbers and finds the max number
'''

a1 = int(input("Enter first number: "))
a2 = int(input("Enter second number: "))
a3 = int(input("Enter third number: "))

def find_max(a1, a2, a3):
    result = max(a1, a2, a3)
    print(f"Max Number among {a1}, {a2}, {a3} is: ", result)

find_max(a1, a2, a3)



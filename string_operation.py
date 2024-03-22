# Find lower, upper and reverse of the string

'''
This code performs string operations like length, lower, upper and reverse of the string
'''

def string_ops(s):
    s_lower = s.lower()
    s_length = len(s)
    s_upper = s.upper()
    s_reverse = s[::-1]

    print(f"Length of the string {s} is", s_length)
    print(f'Lower case of the string {s}', s_lower)
    print(f'Upper case of the string {s}', s_upper)
    print(f'Reverse of the string {s}', s_reverse)

s = input("Enter the string for string operations   :   ")
string_ops(s)

          


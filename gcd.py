'''
Find the greatest common divisor
'''

def compute_gcd(x, y):
    while y:
        x,y = y, x % y
    return x

num1 = int(input('Enter the first: '))
num2 = int(input('Enter the second: '))

print('GCD :', compute_gcd(num1, num2))
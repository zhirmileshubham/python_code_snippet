'''
This code checks if number is prime or not
'''

def is_prime(n):
    if n <=1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n%i==0:
            return False
    return True

num = int(input("Enter number to check for prime number or not: "))

if is_prime(num):
    print("Number is prime")
else:
    print("Number is not prime")

'''
This code generates prime numbers in a given range
'''

def generate_prime(start, end):
    primes = []
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
                else:
                    primes.append(num)
    return primes

start_range = int(input('Enter the start range: '))
end_range = int(input('Enter the end range: '))

print('Prime Numbers:', generate_prime(start_range, end_range))
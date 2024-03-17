'''
This code take 3 input
first principal amount
second rate of intrest
third time period
'''

p = int(input("Enter the principal amount: "))
r = int(input("Enter the rate of intrest: "))
t = int(input("Enter the time period: "))

intrest = (p*r*t)/100
print(f"Simple Intrest:", intrest)
'''
This code checks LCM of given two number
'''

def cal_lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1

    return lcm

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
result = cal_lcm(num1, num2)

print(f"LCM of {num1} and {num2} is", result)

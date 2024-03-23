'''
Below code calculates the number of vowels in provided strings
'''

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    counter = 0

    for char in s:
        if char in vowels:
            counter += 1
    return counter


s = input("Enter the string to check for vowels: ")
result = count_vowels(s)
print(f"number of vowels in input string {s} is", result)

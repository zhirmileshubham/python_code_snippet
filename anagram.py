'''
Below code checks the anagram for two strings
'''

def check_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

string1 = input("Enter first string :")
string2 = input("Enter the second string :")

if check_anagram(string1, string2):
    print("Given string is anagram")
else:
    print("Given string is not anagram")
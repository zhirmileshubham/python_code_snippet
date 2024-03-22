def is_panlindrom(s):
    return s==s[::-1]

s = input("Enter the input string: ")

if is_panlindrom(s):
    print("Given string is palindrom...")
else:
    print("given string is not palindrom...")

    
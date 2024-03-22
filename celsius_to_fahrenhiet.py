def celsius_to_fahrenheit(temp):
    fah = (temp * 9/5) + 32
    print(f'for celsius temperature {temp}, fahrenheit temperature is : ', fah)

temp = float(input("Enter the temperature in Celsius:  "))
celsius_to_fahrenheit(temp)
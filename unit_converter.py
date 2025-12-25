# Conversion menu
print("1. Miles to Kilometers")
print("2. Kilometers to Miles")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")

# Ask the user to choose a conversion
conversion = int(input("What do you want to convert?: "))

# Option 1: Miles → Kilometers
if conversion == 1:
    miles = int(input("How many miles?: "))
    kilometers = round(miles * 1.609344, 2)
    print(str(miles) + " miles = " + str(kilometers) + " kilometers.")

# Option 2: Kilometers → Miles
elif conversion == 2:
    kilometers = int(input("How many kilometers?: "))
    miles = round(kilometers * 0.621371, 2)
    print(str(kilometers) + " kilometers = " + str(miles) + " miles.")

# Option 3: Celsius → Fahrenheit
elif conversion == 3:
    celsius = int(input("How many celsius?: "))
    fahrenheit = round((celsius * 9 / 5) + 32, 2)
    print(str(celsius) + " celsius = " + str(fahrenheit) + " fahrenheit.")

# Option 4: Fahrenheit → Celsius
elif conversion == 4:
    fahrenheit = int(input("How many fahrenheit?: "))
    celsius = round((fahrenheit - 32) * 5 / 9, 2)
    print(str(fahrenheit) + " fahrenheit = " + str(celsius) + " celsius.")

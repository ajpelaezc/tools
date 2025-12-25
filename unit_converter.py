print("1. Miles to Kilometers")
print("2. Kilometers to Miles")
print("3. Celcius to Fahrenheit")
print("4. Fahrenheit to Celcius")
conversion = int(input("What do you want to convert?: "))
if conversion == 1:
    miles = int(input("How many miles?: "))
    kilometers = round(miles * 1.609344, 2)
    print(str(miles) + " miles = " + str(kilometers) + " kilometers.")
elif conversion == 2:
    kilometers = int(input("How many kilometers?: "))
    miles = round(kilometers * 0.621371, 2)
    print(str(kilometers) + " kilometers = " + str(miles) + " miles.")
elif conversion == 3:
    celcius = int(input("How many celcius?: "))
    fahrenheit = round((celcius * 9/5) + 32, 2)
    print(str(celcius) + " celcius = " + str(fahrenheit) + " fahrenheit.")
elif conversion == 4:
    fahrenheit = int(input("How many fahrenheit?: "))
    celcius = round((fahrenheit - 32) * 5/9, 2)
    print(str(fahrenheit) + " fahrenheit = " + str(celcius) + " celcius.")
# Controls whether the program keeps running
keep_running = True

while keep_running:

    # Display conversion menu
    print("Choose a conversion:")
    print("1. Miles → Kilometers")
    print("2. Kilometers → Miles")
    print("3. Celsius → Fahrenheit")
    print("4. Fahrenheit → Celsius")

    # Get conversion choice
    try:
        choice = int(input("Enter option number (1–4): "))
        if choice not in (1, 2, 3, 4):
            print("Please choose a valid option from the menu.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Get value to convert
    try:
        input_value = float(input("Enter the value to convert: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        continue

    # Perform conversion
    if choice == 1:
        result = round(input_value * 1.609344, 2)
        print(f"{input_value} miles = {result} kilometers")

    elif choice == 2:
        result = round(input_value * 0.621371, 2)
        print(f"{input_value} kilometers = {result} miles")

    elif choice == 3:
        result = round((input_value * 9 / 5) + 32, 2)
        print(f"{input_value} °C = {result} °F")

    elif choice == 4:
        result = round((input_value - 32) * 5 / 9, 2)
        print(f"{input_value} °F = {result} °C")

    # Ask if the user wants to continue
    response = input("Convert another value? (yes/no): ").lower()
    if response != "yes":
        keep_running = False

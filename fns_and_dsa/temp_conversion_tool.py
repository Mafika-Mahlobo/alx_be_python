FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 /5

def  convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temp = float(input("Enter the temperature to convert: ").lower())
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

    match unit:
        case "c":
            print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
        case "f":
            print(f"{temp}°F is {convert_to_celsius(temp)}°C")
        case _:
            print(print("Invalid input. Enter C or F"))
except ValueError as err:
    print(f"Invalid value. {err}")
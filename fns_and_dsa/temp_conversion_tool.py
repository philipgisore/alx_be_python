FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return round(celsius, 2)

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return round(fahrenheit, 2)

def main():
    try:
        temp_input = input("Enter the temperature value ").strip()
        temperature = float(temp_input)
        unit = input("Is this in celsius or fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {result}°C")

        elif unit == 'C':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {result}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid temperature value and unit.")

if __name__ == "__main__":
    main()

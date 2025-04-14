def main():
    print('This program converts Fahrenheit to Celsius.')
    fahrenheit : str = input('Enter temperature in Fahrenheit: ')
    fahrenheit : float = float(fahrenheit)
    celsius : float = (fahrenheit - 32) * 5 / 9
    print(f"The Temperature: {fahrenheit}F = {celsius:.2f}C.")


if __name__ == "__main__":
    main()
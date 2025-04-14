def main():
    # Get user input
    number : float = float(input("Enter a number: "))

    # Calculate the square of the number
    square : float = number ** 2

    # Display the result
    print(f"The square of {number} is {square}.")


if __name__ == "__main__":
    main()
def main():
    # Get initial number from user
    curr_value = int(input("Enter a number: "))
    
    # Print initial number without newline
    print(curr_value, end=" ")
    
    # Keep doubling until reaching 100 or greater
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
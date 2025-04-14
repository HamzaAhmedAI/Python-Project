def get_last_element(lst):
    """Returns the last element of the provided list."""

    # Takes the length of the list and minuses 1 since they are zero-indexed (we start counting at 0)
    return lst[len(lst) - 1]

    # The line below works too!!
    # return lst[-1]


def get_lst():
    """Prompts the user to enter one element of the list at a time and returns the resulting list."""
    lst = []
    while True:
        elem = input("Please enter an element of the list or press enter to stop. ")
        if elem == "":
            break
        lst.append(elem)
    return lst

def main():
    lst = get_lst()
    if lst:  # Check if the list is not empty
        print(get_last_element(lst))
    else:
        print("The list is empty.")
        print("The list is empty.")


if __name__ == '__main__':
    main()